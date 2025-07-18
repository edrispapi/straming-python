"""Task example using RabbitMQ as broker"""
from core.celery_app import app

@app.task
def send_email(email, subject, body):
    # ارسال ایمیل با استفاده از صف RabbitMQ
    pass
