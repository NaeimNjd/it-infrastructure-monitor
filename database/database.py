import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "monitor.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            os TEXT NOT NULL
        )
        """
    )

    count = connection.execute("SELECT COUNT(*) FROM servers").fetchone()[0]

    if count == 0:
        connection.executemany(
            "INSERT INTO servers (hostname, ip_address, os) VALUES (?, ?, ?)",
            [
                ("localhost", "127.0.0.1", "Local Monitoring Host"),
                ("dc01-lab", "192.168.10.10", "Windows Server"),
                ("proxmox01-lab", "192.168.10.20", "Proxmox VE"),
            ],
        )

    connection.commit()
    connection.close()


def get_servers():
    connection = get_connection()
    rows = connection.execute(
        "SELECT id, hostname, ip_address, os FROM servers ORDER BY id"
    ).fetchall()
    connection.close()

    return [dict(row) for row in rows]
