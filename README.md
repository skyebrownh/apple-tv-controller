# Apple TV Controller

A Python-based application for controlling multiple Apple TVs from a single interface. Built to eliminate the need for multiple remotes, this tool is designed to run on a touchscreen device like a Raspberry Pi.

## Features

- Scan for Apple TVs on the local network
- Pair with Apple TVs and store credentials securely
- Auto-connect to known devices using saved credentials
- Navigate Apple TV interface with directional controls
- Access common actions like Home, Menu, and Select
- Sleep the device or return to the top menu
- Command-line menu interface using arrow key navigation

> Note: Volume control and wake-on-command support may vary depending on Apple TV setup and HDMI-CEC compatibility.

## Tech Stack

- **Python 3.10+**
- [`pyatv`](https://github.com/postlund/pyatv) – for Apple TV communication
- `asyncio` – for asynchronous device control
- `inquirer` – for interactive terminal menus

## Requirements

- Apple TVs must be on the same local network
- Initial pairing requires accepting a PIN on the Apple TV screen

## Setup

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
    python main.py
    ```

## Roadmap

- Raspberry Pi touchscreen deployment
- Custom UI layer for touch input
- Enhanced error handling and status feedback
- Optional config file support