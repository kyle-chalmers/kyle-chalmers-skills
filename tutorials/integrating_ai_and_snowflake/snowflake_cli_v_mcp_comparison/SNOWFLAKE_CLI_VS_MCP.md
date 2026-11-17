# Snowflake CLI vs MCP

Updated November 17, 2026. Companion to [Claude Code + Snowflake](https://youtu.be/q1y7M5mZkkE).

## Choose by the task

The [Snowflake CLI SQL reference](https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/sql-commands/sql) documents query execution, SQL files and output formats. For repeatable exports, I prefer a command whose output I can save and inspect:

```bash
snow sql -c YOUR_CONNECTION -q "SELECT CURRENT_USER(), CURRENT_ROLE()"
snow sql -c YOUR_CONNECTION -q "SELECT CURRENT_DATE() AS run_date" --format csv > run_date.csv
```

The [Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) exposes configured tools to MCP clients. It supports SQL execution alongside Cortex Analyst, Search and Agent tools. The tools available to a client depend on the server configuration and grants.

| Question | What to check |
|---|---|
| Do I need a local file? | Check the CLI's output formats and the destination path. |
| Does the assistant need discoverable Snowflake tools? | Check the managed MCP server and the client's connector support. |
| What can the connection change? | Inspect its Snowflake role and object grants. Client approval prompts add another check. |
| How much reaches the model? | Inspect the actual tool output and client behavior. Fixed token counts are not a reliable comparison. |

## The original MCP server

The video used [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp). That project now says it is deprecated and no longer maintained, and directs users to Snowflake's managed server. Its setup and limits should not be treated as the managed server's setup and limits.

The [original MCP setup guide](../instructions/SNOWFLAKE_MCP_SETUP.md) remains here for people following the original walkthrough. For a new connection, start with the managed server documentation above.

## Guides and maintained workflow

- [Snowflake CLI setup](../instructions/SNOWFLAKE_CLI_SETUP.md)
- [Original MCP setup](../instructions/SNOWFLAKE_MCP_SETUP.md)
- [Ticketwright](https://github.com/kyle-chalmers/ticketwright), the maintained ticket-driven analysis workflow

No warehouse queries were run for this documentation migration.
