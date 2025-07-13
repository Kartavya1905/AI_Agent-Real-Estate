from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from environment (optional for now)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

def create_user_in_db(user_data):
    """
    Simulates creating a user in the CRM database.
    Replace this later with actual MongoDB logic.
    """
    return {
        "status": "User created using DB URI",
        "db_uri": MONGO_URI,
        "user": user_data
    }
