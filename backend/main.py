from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="AI Accessibility Navigator API")

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.get("/obstacles")
def get_obstacles():
    # Placeholder για την ανάκτηση δεδομένων από τη Firebase Firestore
    return {"message": "Επιστροφή λίστας εμποδίων σε μορφή GeoJSON"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    # Placeholder για την ανάλυση της εικόνας από το YOLOv8
    return {"filename": file.filename, "message": "Η εικόνα ελήφθη επιτυχώς"}