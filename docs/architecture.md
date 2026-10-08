# Architecture

```text
                +----------------------+
                |      Web Browser      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    Flask Web App     |
                |   Python / REST API  |
                +----+-------------+---+
                     |             |
                     v             v
              +-----------+   +-----------+
              |  SQLite   |   |  psutil   |
              | Inventory |   |  Metrics  |
              +-----------+   +-----------+
```

The project is intentionally designed as a small IT lab application.

Future integrations could include:

- Active Directory
- Proxmox API
- VMware vSphere
- SNMP
- Prometheus
- Grafana
- Alerting
