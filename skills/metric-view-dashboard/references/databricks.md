# Databricks reference

Verified end to end on 2026-11-02 with two unrelated Unity Catalog metric views (TPC-H orders and
NYC taxi trips), Claude Dashboards (beta) and the Unity Gateway SQL server.

## Connector

Use the Databricks SQL MCP server Databricks recommends for new integrations, served through Unity
Gateway ([Databricks SQL MCP server](https://docs.databricks.com/aws/en/agents/mcp-tools/databricks-sql)):

- URL: `https://<workspace-host>/ai-gateway/mcp-services/system.ai.dbsql`
- OAuth scope: `ai-gateway`
- Prerequisite: an account admin enables the Unity Gateway beta on the account console Previews page.
- Access: `EXECUTE` on the MCP service, plus `USE CATALOG` and `USE SCHEMA` on `system.ai`.

In Claude: Customize > Connectors > Add > Add custom connector. Choose Sign in now and Use your own
OAuth client, with a Databricks account OAuth app that has the `ai-gateway` scope and Claude's
redirect URLs (`https://claude.ai/api/mcp/auth_callback`, `https://claude.com/api/mcp/auth_callback`).
Set the connector's tools to Always allow, because a dashboard refresh cannot stop to ask for
approval.

Queries run as the signed-in user, so Unity Catalog permissions, row filters and column masks apply
per person. To make the server read-only for everyone, set `disallow_writes` to true in the built-in
`system.ai.dbsql_policy` policy (Beta; needs the Unity Gateway Service Policies workspace preview;
see [Govern an MCP](https://docs.databricks.com/aws/en/ai-gateway/govern-mcp-service)).

### Connectors that do not suit live dashboards

- **Genie (Genie One or a Genie space).** Correct answers in chat, but each dashboard refresh starts a
  Genie conversation, and in testing every refresh ran past the dashboard's load limit of about three
  minutes.
- **The older `/api/2.0/mcp/sql` endpoint.** Claude's custom connector sign-in sends you to
  `<host>/authorize`, a 404, because that endpoint's 401 response carries no `resource_metadata`
  pointer ([claude-ai-mcp#1212](https://github.com/anthropics/claude-ai-mcp/issues/1212)). It works
  with a static `Authorization: Bearer <token>` header on a No sign-in connector, but then everyone
  shares that token's identity.

## Read the definition

```sql
SHOW CREATE TABLE <catalog>.<schema>.<metric_view>;
```

The result contains the YAML: `source`, `dimensions` (name and `expr`) and `measures` (name, `expr`,
optional `comment`).

## Query syntax

- Measures go through `MEASURE(<measure_name>)`, or `agg` on Databricks Runtime 18.1 and above.
- `SELECT *` is not allowed, and a metric view cannot be joined directly at query time.
- Group by dimensions by name; filter with `WHERE` on dimensions, or `MEASURE(x) FILTER (WHERE ...)`
  for one measure.

([Query metric views](https://docs.databricks.com/aws/en/uc-semantics/metric-views/query))

## Query history

Each refresh shows up as new statements from the client "Databricks SQL MCP", under the signed-in
user. Check in the Query History page, or:

```sql
SELECT statement_id, start_time, executed_by, statement_text
FROM system.query.history
WHERE start_time > current_timestamp() - INTERVAL 15 MINUTES
  AND statement_text ILIKE '%<metric_view>%'
ORDER BY start_time DESC;
```

## Known issue: empty tiles after "Updated now"

In testing, the first page Claude generated on every build used a generic Databricks result loader that read this
connector's results (`result.data_typed_array`, cells wrapped as `{str: ...}`) as zero rows, so the
page said it had updated while every tile stayed empty. This prompt fixed it in one turn every time:

```text
The dashboard shows "Updated now", and the warehouse's query history shows the queries finished, but every tile is blank. Check the page against the actual result shape the SQL connector returns and fix it.
```
