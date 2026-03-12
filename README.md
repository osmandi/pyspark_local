# PySpark local development

PySpark in local environment with Docker.

Web interfaces:
- `localhost:8080` = Spark master web UI.
- `localhost:4040` = Spark App UI (available only when a Spark App is running).
- `localhost:18080` = Spark history server.

Spark cluster details (editable in `./docker-compose.yaml`):
- Cluster manager type: Standalone.
- Worker numbers: 2.
- Worker memory: 3G.
