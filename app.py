from flask import Flask, jsonify, render_template
import platform
import socket
import time

import psutil

from database.database import init_db, get_servers

app = Flask(__name__)


def get_local_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "uptime_seconds": int(time.time() - psutil.boot_time()),
    }


@app.route("/")
def dashboard():
    servers = get_servers()
    metrics = get_local_metrics()
    return render_template("dashboard.html", servers=servers, metrics=metrics)


@app.route("/api/servers")
def api_servers():
    return jsonify(get_servers())


@app.route("/api/metrics")
def api_metrics():
    return jsonify(get_local_metrics())


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
