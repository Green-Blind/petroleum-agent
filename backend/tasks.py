from celery_app import app

@app.task
def ping():
    print("pong")