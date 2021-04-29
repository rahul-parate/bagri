from celery import Celery
from demo_app.celery import app
import requests, time


@app.task
def add(x, y):
    return x + y

@app.task(
	autoretry_for=(Exception,),
	retry_backoff=True,
	retry_backoff_max=1800,
	retry_jitter=100,
	max_retries=15)
def retry_task(url):
	res = requests.get(url)
	res = res.json()
	if res.get('status_code') == '200':
		print("success")
		# We can uodate status in database or create a service to do update in database.
		return True

@app.task
def retry_manual_task(
	url,
	max_try=3,
	delay_time=5,
	):
	try:
		res = requests.get(url)
		res = res.json()
		if res.get('status_code') == '200':
			print("success")
			return True
	except Exception as e:
		print(e)
		if max_try > 0:
			time.sleep(delay_time)
			retry_manual_task.delay(
				url=url,
				max_try=max_try-1,
				delay_time=delay_time)
