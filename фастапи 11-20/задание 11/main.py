from fastapi import FastAPI, BackgroundTasks
from tasks import send_email_task

app = FastAPI()

@app.post("/send-email")
def send_email(email: str):
    task = send_email_task.delay(email)
    return {"message": "Email отправлен в очередь", "task_id": task.id} 