import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    # Try to load from environment variable first (for Railway/production)
    firebase_creds_json = os.getenv('FIREBASE_CREDENTIALS')
    
    if firebase_creds_json:
        # Parse JSON from environment variable
        try:
            cred_dict = json.loads(firebase_creds_json)
            cred = credentials.Certificate(cred_dict)
        except json.JSONDecodeError:
            print("Error: FIREBASE_CREDENTIALS is not valid JSON")
            raise
    else:
        # Fallback to file (for local development)
        firebase_key_path = os.path.join("firebase_key.json")
        if os.path.exists(firebase_key_path):
            cred = credentials.Certificate(firebase_key_path)
        else:
            print("Warning: No Firebase credentials found. Set FIREBASE_CREDENTIALS env var or add firebase_key.json")
            cred = None
    
    if cred:
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    else:
        print("Firebase not initialized - no credentials available")
        db = None
else:
    print("Firebase already initialized")
    db = firestore.client()

