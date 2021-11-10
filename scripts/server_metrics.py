import psutil
import time
import csv
import asyncio
from datetime import datetime


async def get_metrics():
	cpu_usage = psutil.cpu_percent()
	memory_usage = psutil.virtual_memory().percent
	timestamp = datetime.now().strftime("%H:%M:%S")
	bytes_sent = psutil.net_io_counters().bytes_sent
	bytes_recv = psutil.net_io_counters().bytes_recv
	return [timestamp, cpu_usage, memory_usage, bytes_sent, bytes_recv]

async def recordMetrics():
	with open('log.csv','w', newline='') as log:
		log_writer = csv.writer(log, delimiter=",")

		while True:
			id_coroutine = get_metrics()
			snapshot = await id_coroutine
			## snapshot = get_metrics()
			print(snapshot)
			log_writer.writerow(snapshot)
			await asyncio.sleep(5)
