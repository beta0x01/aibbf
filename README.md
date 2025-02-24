# AI-Driven Bug Bounty Framework (AIBBF)
![AIBBF Banner](res/logo.png)

The **AI-Driven Bug Bounty Framework (AIBBF)** is a cutting-edge, modular, and professional-grade tool designed for ethical hackers and red-hat teams. It combines the power of artificial intelligence with traditional penetration testing methodologies to provide an unparalleled experience in vulnerability discovery and exploitation.

---

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modules](#modules)
6. [Web UI](#web-ui)
7. [CLI vs Web Framework](#cli-vs-web-framework-comparison)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

AIBBF is a fully modular framework that integrates AI capabilities to enhance the efficiency and effectiveness of bug bounty hunting and penetration testing. Whether you're running it as a command-line interface (CLI) or leveraging its powerful web-based user interface (UI), AIBBF provides real-time insights, customizable execution, and seamless integration into your workflow.

---

## Key Features

### 🛠️ Core Features

- **Modern Web UI**: Real-time statistics, progress bars, logs, and results.
- **Dark Mode / Light Mode Toggle**: Customize the UI to suit your preferences.
- **Modular Design**: Easily add new pentesting modules tailored to your needs.
- **Full CLI & UI Integration**: Run AIBBF as a CLI tool or enable the UI with `-ui`.
- **Customizable Execution**: Choose specific modules to run or execute all modules with `-all`.
- **Live Server on Localhost**: Default port `8088` (configurable with `-port`).
- **Interactive Terminal Logo & Menu**: A sleek and intuitive terminal interface.

### 🛠️ Features in This Legendary Framework

#### 🔹 Real-Time Web UI (Optional)
- Fully interactive dashboard with:
  - **Statistics**: Scans completed, vulnerabilities found, etc.
  - **Progress Tracking**: Modules running, estimated time left.
  - **Log Tracking**: View real-time logs directly from the browser.
  - **Toggle Menus**: Enable/disable modules dynamically.
  - **Light/Dark Mode**: Switch between themes effortlessly.

#### 🔹 Full Automation & AI Integration

- **AI Pentesting Recommendations**: Intelligent suggestions for next steps.
- **AI Exploit Generation**: Automatically craft payloads based on discovered vulnerabilities.
- **AI Fuzzing & Payload Crafting**: Advanced fuzzing techniques powered by machine learning.
- **AI Report Generation**: Export detailed reports in PDF, Markdown, or HTML formats.

#### 🔹 Multi-Module System (Choose What to Run)

- **Recon**:
  - Subdomain scanning
  - WHOIS lookups
  - DNS enumeration
  - ASN analysis
- **Web**:
  - API security testing
  - WAF detection
  - WebSockets and GraphQL analysis
  - XSS and SQLi detection
- **Cloud**:
  - AWS/GCP/Azure misconfiguration scanning
- **Network**:
  - Firewall detection
  - SSRF mapping
  - Port scanning
- **Exploitation**:
  - AI-powered payload crafting
  - Automated exploit execution

#### 🔹 Runs as CLI or Full Web Framework

- **CLI Mode (Default)**: Execute commands directly in the terminal.
- **Web UI Mode (`-ui`)**: Launch a local web app at `http://localhost:8088`.
- **Custom Port (`-port 9090`)**: Specify a different port for the web interface.

---

## Installation

To get started with AIBBF, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/beta0x01/aibbf.git
   cd aibbf
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt # if err: use --break-system-packages
   ```
3. (Optional) Set up a virtual environment for isolated dependency management.
   - Install virtualenv (If Not Already Installed)
      First, ensure that you have the virtualenv package installed. If not, install it using pip:
         ```
         pip install virtualenv
         ```
   - Clone the reposiory and navigate to `aibbf`. 🆙⬆
   - Create Virtual Environment
      - vai `virtualenv`
      ```
      virtualenv venv
      ```
      - or `venv`
      ```
      python -m venv venv
      ```
   - Activate it.
      On Linux/MacOS:
      ```
      source venv/bin/activate
      ```
      On Windows:
      ```
      venv\Scripts\activate
      ```
   - Install Dependencies 🆙⬆
   - Deactivate the Virtual Environment (When Done)
     Once you're done working in the virtual environment, you can deactivate it by running:
      ```
      deactivate
      ```
      
---

## Usage

### CLI Mode

Run AIBBF in the terminal:
```bash
python aibbf.py
```
Specify options:
- Run all modules: `python aibbf.py -all`
- Run specific modules: `python aibbf.py -module recon,web`
- View help: `python aibbf.py -h`
### Web UI Mode

Start the web server:
```bash
python aibbf.py -ui
```
Access the dashboard at [http://localhost:8088](http://localhost:8088/)
```bash
python aibbf.py -ui -port 9090
```
Access the dashboard at [http://localhost:9090](http://localhost:9090/)

---

## Modules
AIBBF is built with a modular architecture, allowing users to extend its functionality easily. Below are the core modules included by default:
- **Recon** : Gather information about the target.
- **Web** : Perform comprehensive web application security assessments.
- **Cloud** : Identify misconfigurations in cloud environments.
- **Network** : Analyze network infrastructure for vulnerabilities.
- **Exploitation** : Automate exploit generation and execution.
- **ALL**: Everything...

To add a new module, create a Python script in the `modules/` directory and define the required functions.

---

## Web UI

The web interface provides a modern and intuitive way to interact with AIBBF. Key features include:

- Real-time updates on scan progress and results.
- Interactive toggles for enabling/disabling modules.
- Detailed logs displayed in the browser.
- Customizable themes (Light/Dark Mode).

---

## CLI vs Web Framework Comparison

| Feature             | CLI Mode               | Web Framework             |
| ------------------- | ---------------------- | ------------------------- |
| Interface           | Terminal               | Browser                   |
| Real-Time Updates   | Logs in terminal       | Dashboard with live stats |
| Module Selection    | Command-line arguments | Dropdown menus            |
| Theme Customization | N/A                    | Light/Dark Mode toggle    |

---

## Contributing

We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request detailing your changes.
Please ensure your code adheres to our coding standards and includes appropriate tests.

---

## License

This project is licensed under the [MIT License](https://github.com/beta0x01/aibbf/LICENSE) . Feel free to use, modify, and distribute AIBBF as per the terms of the license.

---

Thank you for choosing AIBBF! We hope this framework empowers you to take your bug bounty hunting and penetration testing to the next level. If you have any questions or need assistance, please don't hesitate to reach out.

Happy hacking!
