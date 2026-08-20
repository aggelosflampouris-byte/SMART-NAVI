import io
import time
from fastapi import FastAPI, File, UploadFile, BackgroundTasks, Form
from PIL import Image
from ultralytics import YOLO
import firebase_admin
from firebase_admin import credentials, firestore

app = FastAPI(title="AI Accessibility Navigator API")

# 1. Αρχικοποίηση Firebase Firestore
try:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Η σύνδεση με τη Firebase Firestore ολοκληρώθηκε επιτυχώς.")
except Exception as e:
    print(f"Προειδοποίηση: Δεν βρέθηκε το firebase_credentials.json ({e}). Λειτουργία χωρίς βάση.")
    db = None

# 2. Φόρτωση Μοντέλου YOLOv8n
model = YOLO("yolov8n.pt")
CONFIDENCE_THRESHOLD = 0.65

def process_image_and_store(image_bytes: bytes, filename: str, lat: float, lng: float):
    """Ασύγχρονη ανάλυση AI και αποθήκευση στη Firestore σε μορφή GeoJSON."""
    try:
        image = Image.open(io.BytesIO(image_bytes))
        results = model(image, conf=CONFIDENCE_THRESHOLD)
        
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                confidence = float(box.conf[0])
                
                # Κατασκευή αντικειμένου GeoJSON Feature
                geojson_feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lng, lat]  # [Longitude, Latitude] βάσει προτύπου GeoJSON
                    },
                    "properties": {
                        "label": class_name,
                        "confidence": round(confidence, 2),
                        "timestamp": int(time.time()),
                        "source_image": filename
                    }
                }
                
                # Αποθήκευση στη συλλογή 'obstacles' της Firestore
                if db:
                    db.collection("obstacles").add(geojson_feature)
                    print(f"[{filename}] Εμπόδιο {class_name} αποθηκεύτηκε στη Firestore.")
                    
    except Exception as e:
        print(f"Σφάλμα επεξεργασίας/αποθήκευσης: {e}")

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.get("/obstacles")
def get_obstacles():
    """Ανάκτηση όλων των εμποδίων σε μορφή GeoJSON FeatureCollection."""
    print("-> Εκτέλεση GET /obstacles: Ανάκτηση δεδομένων από Firestore...")
    features = []
    if db:
        docs = db.collection("obstacles").stream()
        for doc in docs:
            features.append(doc.to_dict())
            
    print(f"-> Ολοκληρώθηκε: Επιστράφηκαν {len(features)} εμπόδια.")
    return {
        "type": "FeatureCollection",
        "features": features
    }
@app.post("/upload-image")
async def upload_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    lat: float = Form(37.9838),  # Προεπιλεγμένες συντεταγμένες (Demo Mode)
    lng: float = Form(23.7275)
):
    image_bytes = await file.read()
    
    # Εκτέλεση ανάλυσης και αποθήκευσης στο υπόβαθρο
    background_tasks.add_task(process_image_and_store, image_bytes, file.filename, lat, lng)
    
    return {
        "filename": file.filename,
        "status": "processing",
        "location": {"lat": lat, "lng": lng},
        "message": "Η εικόνα ελήφθη. Η ανάλυση και η καταγραφή εκτελούνται στο υπόβαθρο."
    }