from celery import Celery

app = Celery(
    "agent",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["tasks"],
)
app.conf.timezone = "Europe/Paris"