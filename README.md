# pyspark_local

PySpark in local environment with Docker and DevContainers.

Web interfaces:
- `localhost:8080` = Spark master web UI.
- `localhost:4040` = Spark App UI (available only when a Spark App is running).
- `localhost:18080` = Spark history server.

Spark cluster details (editable in `./.devcontainers/docker-compose.yaml`):
- Cluster manager type: Standalone.
- Worker numbers: 2.
- Worker memory: 3G.

Execution:
- Run in DevContainers.
- Execute the Spark Application in `./apps` in the editor directly (if it runs in DevContainers).

Test
