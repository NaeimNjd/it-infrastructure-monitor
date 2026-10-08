# IT Infrastructure Monitor

A small, portfolio-ready infrastructure monitoring dashboard built with Python and Flask.

This project demonstrates practical IT administration concepts: server inventory, resource monitoring, REST API design, SQLite, PowerShell, Docker, and basic web administration.

## Features

- Server inventory with hostname, IP address and operating system
- CPU, RAM and disk monitoring for the local host
- SQLite database
- REST API endpoints
- PowerShell helper script for Windows administrators
- Docker support
- Clean web dashboard

## Technology

Python 3.11+ · Flask · SQLite · psutil · HTML/CSS · Docker · PowerShell

## Project structure

```text
it-infrastructure-monitor/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
├── database/
│   └── database.py
├── docs/
│   └── architecture.md
├── scripts/
│   └── system_info.ps1
├── templates/
│   └── dashboard.html
└── static/
    └── style.css
```

## Run locally

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Start:
```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## API

- `GET /api/servers`
- `GET /api/metrics`

## Docker

```bash
docker compose up --build
```

Then open `http://127.0.0.1:5000`.

## PowerShell

Run on Windows:

```powershell
.\scripts\system_info.ps1
```

## Portfolio purpose

This is a practical IT lab project created to demonstrate infrastructure administration skills in a reproducible environment.

Possible extensions:

- SNMP monitoring
- Windows Server monitoring
- Active Directory inventory
- Proxmox API integration
- VMware monitoring
- Email/Teams alerts
- Authentication and role-based access
- Prometheus/Grafana integration

## Author

Naeim Najafvand Drikvand

IT System Administration / IT Infrastructure
