# Comparison prompts

Use the same task prompt in each tool so the results can be compared.

## Databricks job

```text
I need to set up automated climate data collection for Arizona. Here's what I need:

1. Research what free climate data APIs are available (prefer no authentication required)
2. Create a Python script that fetches monthly weather data for 10 Arizona cities
3. Create a Databricks job configuration (scheduled 3rd of month, 6 AM Phoenix time)
4. The script should aggregate daily data to monthly statistics
5. Include error handling and data validation

Store everything in this folder with a README documenting the solution.
```

## Share project instructions

```text
Read the existing CLAUDE.md in this repository. Create an AGENTS.md containing the same project instructions, leaving CLAUDE.md unchanged. Show me the diff before making further changes.
```
