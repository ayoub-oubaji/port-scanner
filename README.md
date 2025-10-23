cat > README.md <<'EOF'
# 🚀 port-scanner

![GitHub repo size](https://img.shields.io/github/repo-size/ayoub-oubaji/port-scanner)
![GitHub contributors](https://img.shields.io/github/contributors/ayoub-oubaji/port-scanner)
![License](https://img.shields.io/github/license/ayoub-oubaji/port-scanner)
![Language](https://img.shields.io/github/languages/top/ayoub-oubaji/port-scanner)

A simple **multi-threaded TCP port scanner** written in Python.  
**For educational use only — do not scan networks or devices without explicit permission.**

---

## 📌 Table of Contents
- [Overview](#-overview)  
- [Features](#-features)  
- [Requirements](#-requirements)  
- [Usage](#-usage)  
- [Example output](#-example-output)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Contact](#-contact)

---

## 🔍 Overview
`port-scanner` scans TCP ports on one or more targets to discover open services.  
It uses multiple threads to speed up scanning and supports configurable port ranges, timeout and concurrency.

---

## ✨ Features
- ✅ Multi-threaded scanning for faster results  
- ✅ Scan by IP or hostname  
- ✅ Configurable start/end port, timeout and thread count  
- ✅ No external dependencies (uses Python standard library)

---

## ⚙️ Requirements
- Python 3.8+
- Standard libraries: `socket`, `threading`, `argparse`

(Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # only if you add third-party libs
