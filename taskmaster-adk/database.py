from google.cloud import firestore
import os

# Uses the PROJECT_ID from your .env file
db = firestore.Client(project=os.getenv("PROJECT_ID"))

def save_opportunities(student_id, opportunities_text):
    doc_ref = db.collection("students").document(student_id)
    # Merge=True prevents overwriting other student data
    doc_ref.set({
        "tracked_deadlines": opportunities_text
    }, merge=True)