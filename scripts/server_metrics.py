import psutil
import time
import csv
from datetime import datetime


def get_metrics():
	cpu_usage = psutil.cpu_percent()
	memory_usage = psutil.virtual_memory().percent
	timestamp = datetime.now().strftime("%H:%M:%S")
	bytes_sent = psutil.net_io_counters().bytes_sent
	bytes_recv = psutil.net_io_counters().bytes_recv
	disk_usage = psutil.disk_io_counters().busy_time
	packets_dropped_in = psutil.net_io_counters()[6]
	packets_dropped_out = psutil.net_io_counters()[7]


	return [timestamp, cpu_usage, memory_usage, bytes_sent, bytes_recv, disk_usage, packets_dropped_in, packets_dropped_out]


with open('log.csv','w', newline='') as log:
	log_writer = csv.writer(log, delimiter=",")

	while True:
		snapshot = get_metrics()
		print(snapshot)
		log_writer.writerow(snapshot)
		time.sleep(5)
