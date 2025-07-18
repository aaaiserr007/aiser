from celery_app import celery
import time

@celery.task
def send_email_task(email: str):
    print(f"[Celery] Отправка email на {email}...")
    time.sleep(5)  # имитация долгой отправки
    print(f"[Celery] Email на {email} отправлен!")
    return True 