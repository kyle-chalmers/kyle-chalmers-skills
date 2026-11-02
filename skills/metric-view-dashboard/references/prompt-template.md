# Dashboard prompt template

Fill in the four placeholders, then paste the result into a new Claude chat that has the connector
enabled.

```text
Using the {CONNECTOR NAME} connector, build me a live dashboard on the metric view {CATALOG.SCHEMA.VIEW}.
Use its measures with MEASURE() only, never the source tables or your own aggregation.
Tiles:
{ONE LINE PER TILE: title, measure, filters, grain. Example shape: "Average order value: MEASURE(avg_order_value), year 1997"}
Keep every tile live so the Refresh button reruns its query against the warehouse.
Before you hand it over, load each source once and confirm it returns rows; if a source returns
rows but a tile is empty, fix how the page reads the connector's results.
```

Notes:

- Use the connector's exact display name, so Claude does not pick a different one.
- One line per tile keeps the mapping from tile to measure obvious when you check Sources later.
- The last sentence asks Claude to check for the most common failure, a page that reads the results
  in the wrong shape and shows empty tiles while saying it loaded. In testing it did not prevent
  that on the first build, so keep the fix prompt from the warehouse reference file ready.
