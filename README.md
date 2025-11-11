# System Health Checker

A lightweight Python script to monitor system health by checking **disk usage** and **CPU usage**.  
Designed for automation engineers and system administrators, this script provides **logging, alerts, and configurable thresholds**, making it easy to integrate into daily monitoring or automation workflows.

---

## Features

- Checks **free disk space** for one or more disks.
- Checks **CPU usage** over a configurable interval.
- Logs results with **timestamps** to a log file (`system_health.log`).
- Provides **console output** for quick system health checks.
- Configurable thresholds for **disk and CPU usage**.
- Handles errors gracefully (missing disks, `psutil` issues).

---

## Requirements

- Python 3.6+
- [psutil](https://pypi.org/project/psutil/) library

Install psutil:

```bash
python3 -m pip install psutil
