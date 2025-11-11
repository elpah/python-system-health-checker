#!/usr/bin/env python3

import shutil
import psutil
import logging
from datetime import datetime

DISKS_TO_CHECK = ["/"]
DISK_THRESHOLD = 20   
CPU_THRESHOLD = 75
LOG_FILE = "system_health.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_disk_usage(disk, threshold):
    try:
        du = shutil.disk_usage(disk)
        free_percent = round(du.free / du.total * 100, 2)
        logging.info(f"Disk {disk}: {free_percent}% free")
        return free_percent > threshold
    except FileNotFoundError:
        logging.error(f"Disk path {disk} not found.")
        return False

def check_cpu_usage(threshold):
    try:
        cpu_usage = psutil.cpu_percent(1)
        logging.info(f"CPU usage: {cpu_usage}%")
        return cpu_usage < threshold
    except Exception as e:
        logging.error(f"Error checking CPU usage: {e}")
        return False

def main():
    healthy = True

    for disk in DISKS_TO_CHECK:
        if not check_disk_usage(disk, DISK_THRESHOLD):
            healthy = False
            logging.warning(f"Disk {disk} below threshold!")

    if not check_cpu_usage(CPU_THRESHOLD):
        healthy = False
        logging.warning("CPU usage above threshold!")

    if healthy:
        logging.info("System is healthy ")
        print("System is healthy ")
    else:
        logging.warning("System has issues ")
        print("System has issues Check log for details.")

if __name__ == "__main__":
    main()
