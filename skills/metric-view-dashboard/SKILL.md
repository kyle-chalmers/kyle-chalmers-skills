---
name: metric-view-dashboard
description: >-
  Build a live Claude Dashboard on a governed metric definition (a Databricks Unity Catalog metric
  view) and prove its numbers. Use when the user wants a dashboard that reads their metric view,
  says "build a live dashboard on my metric view", "make a Claude dashboard from sales_metrics",
  "check that my dashboard matches the metric view", or "prove this dashboard is live". Reads the
  view's own definition, writes a MEASURE()-only dashboard prompt, generates independent tie-out
  queries and a refresh check, and asks before any write.
---

# Live dashboard on a metric view

A dashboard is only as right as the definition underneath it. This skill points a Claude Dashboard
at a governed metric definition, so every tile asks the warehouse for the stored measure instead of
re-deriving the math, and then checks two things: that the tiles match queries written independently
of the dashboard, and that a refresh actually reruns them.

The procedure below works for any metric view. It never assumes particular measure names, columns,
dates or filters: everything comes from the definition the user points at. Warehouse-specific
details (connector address, query syntax, how to see query history, known issues) live in one
reference file per warehouse. Today that is [references/databricks.md](references/databricks.md).

## What you need

- A metric view the user can query, named in full (`catalog.schema.view`).
- A SQL connector to the warehouse that Claude Dashboards can use for live queries. On Databricks
  that is the Unity Gateway SQL server; see the reference file for setup and the connectors that do
  not work well for live refresh.
- A Claude plan with Dashboards. Dashboards are built in a Claude chat, not in a terminal.

If any of these is missing, stop and say which one, with the setup step from the reference file.

## Procedure

Run these in order. Each step says what to show the user before moving on.

### 1. Read the definition

Load the metric view's definition through the connector (the reference file has the exact
statement). List back to the user:

- the source table or query it reads,
- every dimension, with its expression,
- every measure, with its expression and any comment.

Do not guess from the view's name or from column names in the source table. If the definition cannot
be read, stop: without it there is nothing governed to build on.

### 2. Choose the tiles

Ask what the dashboard is for. If the user has no preference, propose three to five tiles drawn only
from the measures and dimensions in step 1, and prefer a mix that exercises the definition:

- one ratio or derived measure (the kind most often mis-computed by hand),
- one measure under a filter on a dimension,
- one measure over a time window, if the view has a date dimension,
- optionally one trend: a measure grouped by a time dimension.

Name each tile with its exact measure, filters and grain. Confirm the list before writing the prompt.

### 3. Write the dashboard prompt

Fill in [references/prompt-template.md](references/prompt-template.md) with the connector name, the
metric view, and the confirmed tiles. Hand the user the filled prompt to paste into a new chat (or
use it directly if you are running inside that chat). The template tells Claude to use `MEASURE()`
only, to keep every tile live, and to confirm each source returns rows before handing the dashboard
over.

### 4. Write the expected values first

Before looking at any tile, write two queries per tile and run them:

- **Through the metric view**: the measure with `MEASURE()`, with the tile's filters and grain.
- **Independent of the metric view**: the same number computed directly from the source table, using
  the measure's expression from step 1, with identical filters, grain, date boundaries, null handling
  and rounding.

The two must agree. If they do not, the problem is in the definition or the filters, not the
dashboard: report it and stop. Keep both result sets; they are the reference for step 5.

### 5. Check the dashboard

Once the dashboard renders:

- Open each tile's query (the dashboard's Sources) and confirm it reads the metric view with
  `MEASURE()` (or the warehouse's equivalent) and not the source table with its own aggregation. A
  tile that rewrote the math fails, whatever its number says.
- Compare each tile to the step 4 values. Report each as matched or not, with both numbers.
- Expect the first render to come back empty: the page says it loaded but every tile is blank,
  because it misread the connector's results. In testing this happened on every first build, on two
  different metric views, even with the template's warning line, and the one-line fix prompt in the
  reference file worked each time. Send it before judging the tiles.

### 6. Prove it is live

Pick the least invasive check that still proves a rerun, and ask before anything that writes:

1. **Read-only (default).** Click Refresh and confirm the warehouse received new queries for the
   dashboard's sources (query history, with new statement IDs and start times after the click) and
   that the dashboard's refresh time changed. This proves the queries reran. It does not prove the
   tiles would follow a data change.
2. **Controlled change on a disposable table.** Only if the user confirms the metric view's source is
   theirs to modify (a demo or scratch table): insert one clearly marked row with an obvious value,
   compute the new expected values with step 4's queries, click Refresh, compare, then delete the row
   and refresh again. Show the exact INSERT and DELETE and wait for a yes before running them.
3. **Controlled change on a copy.** If the source is shared or production: copy it into a scratch
   schema, create a metric view with the same definition over the copy, point a dashboard at that,
   and run check 2 there. Drop the scratch objects afterwards.

Never insert into a production table to test a dashboard.

### 7. Report

One short report: the metric view and connector, each tile with its measure and match result, the
live check used and what it showed (statement IDs, before and after values), and anything that
failed with the fix. Say plainly what was not verified, such as permissions for a second viewer.

## Rules

- The definition in the warehouse is the source of truth. If the user asks for a number the view
  does not define, say so and offer to add a measure; do not compute it ad hoc in the dashboard.
- Every write needs the user's explicit yes, with the exact statement shown first.
- Use the user's own sign-in where the connector supports it, so their permissions apply. A shared
  identity (such as a service principal) is a deliberate choice with a stated trade-off.
- Report observed results, not expected ones. A tile is "matched" only after both numbers are seen.

## Other warehouses

The steps above do not depend on Databricks. To use them with another semantic layer (a Snowflake
semantic view, a dbt metric), add a reference file for it that answers the same questions as
`references/databricks.md`: how to connect a live SQL connector, how to read the definition, the
query syntax for a measure, how to see query history, and known issues. Only Databricks has been
tested end to end so far.
