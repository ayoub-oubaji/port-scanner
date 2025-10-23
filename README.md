# port-scanner

A simple multi-threaded TCP port scanner written in Python.  
**For educational use only — do not scan networks or devices without explicit permission.**

## Overview
`port-scanner` scans TCP ports on one or more targets to discover open services.  
It uses threads to speed up scanning and supports configurable port ranges, timeouts and concurrency.

## Features
- Multi-threaded scanning for faster results
- Scan by IP or hostname
- Configurable start/end port, timeout and thread count
- Lightweight and dependency-free (uses Python standard library)

## Requirements
- Python 3.8 or newer
- Standard libraries: `socket`, `threading`, `argparse`

(Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # only if you add third-party libs

