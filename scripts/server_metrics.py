import psutil
import time
import csv
from datetime import datetime
import threading

def get_metrics():
	cpu_usage = psutil.cpu_percent()
	memory_usage = psutil.virtual_memory().percent
	timestamp = datetime.now().strftime("%H:%M:%S")
	bytes_sent = psutil.net_io_counters().bytes_sent
	bytes_recv = psutil.net_io_counters().bytes_recv
	return [timestamp, cpu_usage, memory_usage, bytes_sent, bytes_recv]


def record_metrics():
	writer_lock = threading.Lock()

	with open('log.csv', 'w+', newline='') as log:
		log_writer = csv.writer(log, delimiter=",")

		while True:
			snapshot = get_metrics()
			print(snapshot)
			with writer_lock:
				log_writer.writerow(snapshot)
			time.sleep(5)
