# System Health Checker

A lightweight Python script to monitor system health by checking **disk usage** and **CPU usage**.  
This script provides **logging, alerts, and configurable thresholds**, making it easy to integrate into daily monitoring or automation workflows.

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
```
## Usage

- Make the script executable:
  
```bash
chmod +x disk_health_check.py
```
- Run the script:
  
```bash
./disk_health_check.py
```
- or using Python directly:

```bash
python3 disk_health_check.py
```

- Check console output for immediate system health:
```bash
System is healthy
or
System has issues ❌ Check log for details.
```

- Review detailed logs in system_health.log

## Configuration

- Modify these variables at the top of the script to customize:
```bash
DISKS_TO_CHECK = ["/"]          # List of disk paths to monitor
DISK_THRESHOLD = 20             # Minimum free disk percentage
CPU_THRESHOLD = 75              # Maximum CPU usage percentage
LOG_FILE = "system_health.log"  # Path to log file
```

## Example Log Output
```bash
2025-11-11 10:09:15,123 - INFO - Disk /: 45.67% free
2025-11-11 10:09:16,234 - INFO - CPU usage: 34.5%
2025-11-11 10:09:16,234 - INFO - System is healthy ✅
```
## Future Improvements

- Add email or Slack notifications for warnings.
- Monitor multiple servers remotely via SSH.
- Include additional metrics (memory usage, CPU temperature, network usage).
- Run as a scheduled cron job for continuous monitoring.

  ## License
  This project is licensed under the MIT License.



