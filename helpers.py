from datetime import datetime

def get_timestamp():
    return datetime.utcnow().isoformat()

def mask_email(email):
    if "@" in email:
        name, domain = email.split("@")
        return f"{name[0]}***@{domain}"
    return email
