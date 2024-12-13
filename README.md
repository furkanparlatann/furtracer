# FurTracer

**FurTracer** is a lightweight device monitoring tool that tracks the status of devices via ping and displays their status in a web-based table. Devices are dynamically updated in real-time using WebSocket technology.

## Features

- Real-time device status updates (online/offline).
- Displays devices in a paginated, multi-column layout for better readability.
- Easy to configure and deploy as a service.

---

## File Structure

- **Python Script**: `/etc/furtracer/furtracer.py`
- **HTML Template**: `/etc/furtracer/templates/index.html`
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
   git clone https://github.com/yourusername/furtracer.git
   cd furtracer
   ```

2. **Install Dependencies**
   Install required Python modules:
   ```bash
   pip install flask flask-socketio eventlet
   ```

3. **Setup File Locations**
   - Move the files to the correct locations:
     ```bash
     sudo mkdir -p /opt/furtracer/templates
     sudo cp furtracer.py /opt/furtracer/furtracer.py
     sudo cp index.html /opt/furtracer/templates/index.html
     sudo cp furtracer.service /etc/systemd/system/furtracer.service
     ```

4. **Enable and Start the Service**
   - Reload systemd to recognize the new service:
     ```bash
     sudo systemctl daemon-reload
     ```
   - Enable the service to start on boot:
     ```bash
     sudo systemctl enable furtracer.service
     ```
   - Start the service:
     ```bash
     sudo systemctl start furtracer.service
     ```

5. **Access the Application**
   - Open a web browser and visit `http://<server-ip>:<your_port>`.

---

## Configuration

### Adding Devices
Modify the `devices` list in `furtracer.py` to include the IPs of devices you want to monitor:
```python
devices = [
    {'ip': '192.168.1.1'},
    {'ip': '8.8.8.8'},
    # Add more devices here
]
```

### Change Default Port
To run on a port other than 80, modify the `app.run` line in `furtracer.py`:
```python
app.run(host="0.0.0.0", port=<your_port>)
```

---

## Contributing

Feel free to submit issues or pull requests to enhance the project. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
