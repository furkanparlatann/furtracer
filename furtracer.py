import subprocess
import threading
import time
import concurrent.futures
from flask import Flask, render_template

# Flask Setup 
app = Flask(__name__)

devices = [
        {'ip': '10.34.99.200'},
        {'ip': '10.255.1.1'},
        {'ip': '10.255.1.2'},
        {'ip': '10.255.1.3'},
        {'ip': '10.255.1.11'},
        {'ip': '10.255.1.12'},
        {'ip': '10.255.1.13'},
        {'ip': '10.255.1.14'},
        {'ip': '10.255.1.15'},
        {'ip': '10.255.1.16'},
        {'ip': '10.255.1.17'},
        {'ip': '10.255.1.18'},
        {'ip': '10.255.1.19'},
        {'ip': '10.255.1.20'},
        {'ip': '10.255.1.101'},
        {'ip': '10.255.1.102'},
        {'ip': '10.255.1.103'},
        {'ip': '10.255.1.201'},
        {'ip': '10.255.1.202'},
        {'ip': '10.255.1.203'},
        {'ip': '10.255.1.204'},
        {'ip': '10.255.2.1'},
        {'ip': '10.255.2.2'},
        {'ip': '10.255.2.3'},
        {'ip': '10.255.2.11'},
        {'ip': '10.255.2.12'},
        {'ip': '10.255.2.13'},
        {'ip': '10.255.2.14'},
        {'ip': '10.255.2.15'},
        {'ip': '10.255.2.16'},
        {'ip': '10.255.2.17'},
        {'ip': '10.255.2.18'},
        {'ip': '10.255.2.19'},
        {'ip': '10.255.2.20'},
        {'ip': '10.255.2.101'},
        {'ip': '10.255.2.102'},
        {'ip': '10.255.2.103'},
        {'ip': '10.255.2.201'},
        {'ip': '10.255.2.202'},
        {'ip': '10.255.2.203'},
        {'ip': '10.255.2.204'},
        {'ip': '10.255.3.1'},
        {'ip': '10.255.3.2'},
        {'ip': '10.255.3.3'},
        {'ip': '10.255.3.11'},
        {'ip': '10.255.3.12'},
        {'ip': '10.255.3.13'},
        {'ip': '10.255.3.14'},
        {'ip': '10.255.3.15'},
        {'ip': '10.255.3.16'},
        {'ip': '10.255.3.17'},
        {'ip': '10.255.3.18'},
        {'ip': '10.255.3.19'},
        {'ip': '10.255.3.20'},
        {'ip': '10.255.3.101'},
        {'ip': '10.255.3.102'},
        {'ip': '10.255.3.103'},
        {'ip': '10.255.3.201'},
        {'ip': '10.255.3.202'},
        {'ip': '10.255.3.203'},
        {'ip': '10.255.3.204'},
        {'ip': '10.255.4.1'},
        {'ip': '10.255.4.2'},
        {'ip': '10.255.4.3'},
        {'ip': '10.255.4.11'},
        {'ip': '10.255.4.12'},
        {'ip': '10.255.4.13'},
        {'ip': '10.255.4.14'},
        {'ip': '10.255.4.15'},
        {'ip': '10.255.4.16'},
        {'ip': '10.255.4.17'},
        {'ip': '10.255.4.18'},
        {'ip': '10.255.4.18'},
        {'ip': '10.255.4.19'},
        {'ip': '10.255.4.20'},
        {'ip': '10.255.4.101'},
        {'ip': '10.255.4.102'},
        {'ip': '10.255.4.103'},
        {'ip': '10.255.4.201'},
        {'ip': '10.255.4.202'},
        {'ip': '10.255.4.203'},
        {'ip': '10.255.4.204'},
        {'ip': '10.255.5.1'},
        {'ip': '10.255.5.2'},
        {'ip': '10.255.5.3'},
        {'ip': '10.255.5.11'},
        {'ip': '10.255.5.12'},
        {'ip': '10.255.5.13'},
        {'ip': '10.255.5.14'},
        {'ip': '10.255.5.15'},
        {'ip': '10.255.5.16'},
        {'ip': '10.255.5.17'},
        {'ip': '10.255.5.18'},
        {'ip': '10.255.5.19'},
        {'ip': '10.255.5.20'},
        {'ip': '10.255.5.101'},
        {'ip': '10.255.5.102'},
        {'ip': '10.255.5.103'},
        {'ip': '10.255.5.201'},
        {'ip': '10.255.5.202'},
        {'ip': '10.255.5.203'},
        {'ip': '10.255.5.204'},
        {'ip': '10.255.6.1'},
        {'ip': '10.255.6.2'},
        {'ip': '10.255.6.3'},
        {'ip': '10.255.6.11'},
        {'ip': '10.255.6.12'},
        {'ip': '10.255.6.13'},
        {'ip': '10.255.6.14'},
        {'ip': '10.255.6.15'},
        {'ip': '10.255.6.16'},
        {'ip': '10.255.6.17'},
        {'ip': '10.255.6.18'},
        {'ip': '10.255.6.19'},
        {'ip': '10.255.6.20'},
        {'ip': '10.255.6.101'},
        {'ip': '10.255.6.102'},
        {'ip': '10.255.6.103'},
        {'ip': '10.255.6.201'},
        {'ip': '10.255.6.202'},
        {'ip': '10.255.6.203'},
        {'ip': '10.255.6.204'},
        {'ip': '10.255.7.1'},
        {'ip': '10.255.7.2'},
        {'ip': '10.255.7.3'},
        {'ip': '10.255.7.11'},
        {'ip': '10.255.7.12'},
        {'ip': '10.255.7.13'},
        {'ip': '10.255.7.14'},
        {'ip': '10.255.7.15'},
        {'ip': '10.255.7.16'},
        {'ip': '10.255.7.17'},
        {'ip': '10.255.7.18'},
        {'ip': '10.255.7.19'},
        {'ip': '10.255.7.20'},
        {'ip': '10.255.7.101'},
        {'ip': '10.255.7.102'},
        {'ip': '10.255.7.103'},
        {'ip': '10.255.7.201'},
        {'ip': '10.255.7.202'},
        {'ip': '10.255.7.203'},
        {'ip': '10.255.7.204'},
        {'ip': '10.255.8.1'},
        {'ip': '10.255.8.2'},
        {'ip': '10.255.8.3'},
        {'ip': '10.255.8.11'},
        {'ip': '10.255.8.12'},
        {'ip': '10.255.8.13'},
        {'ip': '10.255.8.14'},
        {'ip': '10.255.8.15'},
        {'ip': '10.255.8.16'},
        {'ip': '10.255.8.16'},
        {'ip': '10.255.8.17'},
        {'ip': '10.255.8.18'},
        {'ip': '10.255.8.19'},
        {'ip': '10.255.8.20'},
        {'ip': '10.255.8.101'},
        {'ip': '10.255.8.102'},
        {'ip': '10.255.8.103'},
        {'ip': '10.255.8.201'},
        {'ip': '10.255.8.202'},
        {'ip': '10.255.8.203'},
        {'ip': '10.255.8.204'},
        {'ip': '10.255.9.1'},
        {'ip': '10.255.9.2'},
        {'ip': '10.255.9.3'},
        {'ip': '10.255.9.11'},
        {'ip': '10.255.9.12'},
        {'ip': '10.255.9.13'},
        {'ip': '10.255.9.14'},
        {'ip': '10.255.9.15'},
        {'ip': '10.255.9.16'},
        {'ip': '10.255.9.17'},
        {'ip': '10.255.9.18'},
        {'ip': '10.255.9.19'},
        {'ip': '10.255.9.20'},
        {'ip': '10.255.9.101'},
        {'ip': '10.255.9.102'},
        {'ip': '10.255.9.103'},
        {'ip': '10.255.9.201'},
        {'ip': '10.255.9.202'},
        {'ip': '10.255.9.203'},
        {'ip': '10.255.9.204'},
        {'ip': '10.255.10.1'},
        {'ip': '10.255.10.2'},
        {'ip': '10.255.10.3'},
        {'ip': '10.255.10.11'},
        {'ip': '10.255.10.12'},
        {'ip': '10.255.10.13'},
        {'ip': '10.255.10.14'},
        {'ip': '10.255.10.15'},
        {'ip': '10.255.10.16'},
        {'ip': '10.255.10.17'},
        {'ip': '10.255.10.18'},
        {'ip': '10.255.10.19'},
        {'ip': '10.255.10.20'},
        {'ip': '10.255.10.101'},
        {'ip': '10.255.10.102'},
        {'ip': '10.255.10.103'},
        {'ip': '10.255.10.201'},
        {'ip': '10.255.10.202'},
        {'ip': '10.255.10.203'},
        {'ip': '10.255.10.204'},
        {'ip': '10.255.11.1'},
        {'ip': '10.255.11.2'},
        {'ip': '10.255.11.3'},
        {'ip': '10.255.11.11'},
        {'ip': '10.255.11.12'},
        {'ip': '10.255.11.13'},
        {'ip': '10.255.11.14'},
        {'ip': '10.255.11.15'},
        {'ip': '10.255.11.16'},
        {'ip': '10.255.11.17'},
        {'ip': '10.255.11.18'},
        {'ip': '10.255.11.19'},
        {'ip': '10.255.11.20'},
        {'ip': '10.255.11.101'},
        {'ip': '10.255.11.102'},
        {'ip': '10.255.11.103'},
        {'ip': '10.255.11.201'},
        {'ip': '10.255.11.202'},
        {'ip': '10.255.11.203'},
        {'ip': '10.255.11.204'},
        {'ip': '10.255.12.1'},
        {'ip': '10.255.12.2'},
        {'ip': '10.255.12.3'},
        {'ip': '10.255.12.11'},
        {'ip': '10.255.12.12'},
        {'ip': '10.255.12.13'},
        {'ip': '10.255.12.14'},
        {'ip': '10.255.12.15'},
        {'ip': '10.255.12.16'},
        {'ip': '10.255.12.17'},
        {'ip': '10.255.12.18'},
        {'ip': '10.255.12.19'},
        {'ip': '10.255.12.20'},
        {'ip': '10.255.12.101'},
        {'ip': '10.255.12.102'},
        {'ip': '10.255.12.103'},
        {'ip': '10.255.12.201'},
        {'ip': '10.255.12.202'},
        {'ip': '10.255.12.203'},
        {'ip': '10.255.12.204'},
        {'ip': '10.255.13.1'},
        {'ip': '10.255.13.2'},
        {'ip': '10.255.13.3'},
        {'ip': '10.255.13.11'},
        {'ip': '10.255.13.12'},
        {'ip': '10.255.13.13'},
        {'ip': '10.255.13.14'},
        {'ip': '10.255.13.15'},
        {'ip': '10.255.13.16'},
        {'ip': '10.255.13.17'},
        {'ip': '10.255.13.18'},
        {'ip': '10.255.13.19'},
        {'ip': '10.255.13.20'},
        {'ip': '10.255.13.101'},
        {'ip': '10.255.13.102'},
        {'ip': '10.255.13.103'},
        {'ip': '10.255.13.201'},
        {'ip': '10.255.13.202'},
        {'ip': '10.255.13.203'},
        {'ip': '10.255.13.204'},
        {'ip': '10.255.14.1'},
        {'ip': '10.255.14.2'},
        {'ip': '10.255.14.3'},
        {'ip': '10.255.14.11'},
        {'ip': '10.255.14.12'},
        {'ip': '10.255.14.13'},
        {'ip': '10.255.14.14'},
        {'ip': '10.255.14.15'},
        {'ip': '10.255.14.16'},
        {'ip': '10.255.14.17'},
        {'ip': '10.255.14.18'},
        {'ip': '10.255.14.19'},
        {'ip': '10.255.14.20'},
        {'ip': '10.255.14.101'},
        {'ip': '10.255.14.102'},
        {'ip': '10.255.14.103'},
        {'ip': '10.255.14.201'},
        {'ip': '10.255.14.202'},
        {'ip': '10.255.14.203'},
        {'ip': '10.255.14.204'},
        {'ip': '10.255.15.1'},
        {'ip': '10.255.15.2'},
        {'ip': '10.255.15.3'},
        {'ip': '10.255.15.11'},
        {'ip': '10.255.15.12'},
        {'ip': '10.255.15.13'},
        {'ip': '10.255.15.14'},
        {'ip': '10.255.15.15'},
        {'ip': '10.255.15.16'},
        {'ip': '10.255.15.17'},
        {'ip': '10.255.15.18'},
        {'ip': '10.255.15.19'},
        {'ip': '10.255.15.20'},
        {'ip': '10.255.15.101'},
        {'ip': '10.255.15.102'},
        {'ip': '10.255.15.103'},
        {'ip': '10.255.15.201'},
        {'ip': '10.255.15.202'},
        {'ip': '10.255.15.203'},
        {'ip': '10.255.15.204'},
        {'ip': '10.255.16.1'},
        {'ip': '10.255.16.2'},
        {'ip': '10.255.16.3'},
        {'ip': '10.255.16.11'},
        {'ip': '10.255.16.12'},
        {'ip': '10.255.16.13'},
        {'ip': '10.255.16.14'},
        {'ip': '10.255.16.15'},
        {'ip': '10.255.16.15'},
        {'ip': '10.255.16.16'},
        {'ip': '10.255.16.17'},
        {'ip': '10.255.16.18'},
        {'ip': '10.255.16.19'},
        {'ip': '10.255.16.20'},
        {'ip': '10.255.16.101'},
        {'ip': '10.255.16.102'},
        {'ip': '10.255.16.103'},
        {'ip': '10.255.16.201'},
        {'ip': '10.255.16.202'},
        {'ip': '10.255.16.203'},
        {'ip': '10.255.16.204'}
]




def ping_device(device):
    """
    Pings a device and updates its status.
    """
    try:
        output = subprocess.run(
            ["ping", "-c", "1", "-W", "2", device["ip"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        device["status"] = "online" if output.returncode == 0 else "offline"
    except Exception:
        device["status"] = "offline"


def ping_all_devices():
    """
    Continuously ping all devices in the list using a thread pool.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(devices)) as executor:
        while True:#+
            # Submit all ping tasks at once
            future_to_device = {executor.submit(ping_device, device): device for device in devices}
            # Wait for all tasks to complete
            concurrent.futures.wait(future_to_device)
#+
            time.sleep(0.2)  # Wait 0.2 seconds before starting the next round of pings


@app.route("/")
def ping_status():
    """
    Endpoint to display device statuses in a user-friendly table.
    """
    return render_template("index.html", statuses=devices)

@app.route("/api/status")
def api_status():
    """
    API endpoint to provide device statuses in JSON format.
    """
    return {"statuses": devices}

if __name__ == "__main__":
    # Start the pinging loop in a background thread
    threading.Thread(target=ping_all_devices, daemon=True).start()

    # Start the Flask web server
    app.run(host="0.0.0.0", port=3434)
