from celery import Celery
import sqlalchemy

app = Celery('tasks', broker='amqp://localhost//', backend='db+postgresql://postgres:root@localhost/workers_db')

@app.task
def reverse(string):
	return string[::-1]
