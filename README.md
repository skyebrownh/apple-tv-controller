# Apple TV Controller

A custom-built controller app that lets you control multiple Apple TVs from a single touchscreen interface. Designed for deployment on a Raspberry Pi with a 7" display, this app removes the need for juggling multiple remotes in shared spaces like living rooms or media centers.

## 🖥️ Features

- Control multiple Apple TVs from a single interface
- Button-based UI optimized for 800×480 screen resolution
- Supports core remote functionality:
  - Navigation (up, down, left, right)
  - Select, Home, Previous, Play/Pause
  - Sleep mode (power off)
- Manual Connect / Disconnect per device
- Visual interface closely mimics a physical Apple TV remote
- Works over Wi-Fi using [pyatv](https://github.com/postlund/pyatv)

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python 3.13)
- **Frontend:** HTML + TailwindCSS + Vanilla JavaScript
- **Apple TV Control:** pyatv
- **Target Hardware:** Raspberry Pi (with 7" touchscreen)

## 🚀 Getting Started (Local)
### Requirements

- Apple TVs must be on the same local network
- Initial pairing requires accepting a PIN on the Apple TV screen

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/skyebrownh/apple-tv-controller.git
   cd apple-tv-controller
   ```

2. (Optional but recommended) Create a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app

    ```bash
    fastapi main.py
    ```

5. Open in browser

    - Visit http://localhost:8000

6. Connect to a device

    - Click the "connect" (link icon) for the Apple TV you want to control
    - Multiple devices can be connected simultaneously
    - Use the interface to interact with your Apple TVs

### Development Notes
- You must pair your Apple TVs using pyatv before using the interface
- Device credentials are saved locally using pyatv's default `~/.pyatv.conf`
- Each session currently requires manual connection; auto-connect coming soon

## 📦 Deployment Plan

The app is designed for installation on a Raspberry Pi running a lightweight Linux OS. The backend runs locally and serves the UI through a browser on the Pi’s 7" touchscreen. FastAPI handles all interactions with the Apple TV devices.