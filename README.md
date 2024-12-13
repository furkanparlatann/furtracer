# FurTracer

**FurTracer** is a lightweight device monitoring tool that tracks the status of devices via ping and displays their status in a web-based table. Devices are dynamically updated in real-time using WebSocket technology.

## Features

- Real-time device status updates (online/offline).
- Displays devices in a paginated, multi-column layout for better readability.
- Easy to configure and deploy as a service.

---

## File Structure

- **Python Script**: `/opt/furtracer/furtracer.py`
- **HTML Template**: `/opt/furtracer/templates/index.html`
- **Service File**: `/etc/systemd/system/furtracer.service`

---

## Requirements

- Python 3.x
- Flask
- Socket.IO (Python and JavaScript versions)
- Systemd (for running as a service)

---

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/furkanparlatann/furtracer.git
   cd furtracer
