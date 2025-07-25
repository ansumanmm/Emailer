import json, os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

def send_email():
    with open("todos.json") as f:
        todos = json.load(f)
    undone = [t["text"] for t in todos if not t["done"]]
    if not undone:
        print("No undone tasks.")
        return

    text = "\n".join(f"• {t}" for t in undone)

    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=os.getenv("TO_EMAIL"),
        subject="Unfinished Tasks Today",
        plain_text_content=text
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(message)
        print("✅ Email sent")
    except Exception as e:
        print("❌ Error sending email:", e)

if __name__ == "__main__":
    send_email()
