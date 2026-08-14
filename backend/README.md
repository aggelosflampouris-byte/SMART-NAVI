# SMART-NAVI Backend

This is the backend for the SMART-NAVI application, built with Python and FastAPI.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3.8+ installed on your machine.

We strongly recommend using a virtual environment to manage project dependencies. To create and activate a virtual environment, run the following commands from the `backend` directory:

```bash
# Create (only once) a virtual environment named 'venv'
python3 -m venv venv

# Activate (or keep it activated in every installing and running anything) the virtual environment
# On macOS and Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate

# Deactivate the virtual environment
deactivate
```


### Installation

1.  **Navigate to the backend directory**:
    ```bash
    cd SMART-NAVI/backend
    ```

2.  **Install dependencies**:
    This command reads the `requirements.txt` file and installs the required Python packages (like FastAPI and Uvicorn).
    ```bash
    pip install -r requirements.txt
    ```
    > **Note:** A `requirements.txt` file is not yet present. I can help you create one based on the current `main.py`.

## Running the Development Server

Once the dependencies are installed, you can start the development server:

```bash
uvicorn main:app --reload
```

This command will start the FastAPI application with Uvicorn, a lightning-fast ASGI server.

*   `main:app` refers to the `app` instance in the `main.py` file.
*   `--reload` makes the server restart after code changes.

The API will be available at `http://127.0.0.1:8000`.

You can also access the interactive API documentation (provided by Swagger UI) at `http://127.0.0.1:8000/docs`.

## API Endpoints

Here is a brief overview of the available API endpoints:

### `GET /`

*   **Description**: A root endpoint to check if the backend is running.
*   **Response**:
    ```json
    {
      "status": "Backend is running"
    }
    ```

### `GET /obstacles`

*   **Description**: (Placeholder) Retrieves a list of obstacles in GeoJSON format. This will integrate with Firebase Firestore.

### `POST /upload-image`

*   **Description**: (Placeholder) Accepts an image file for obstacle detection. This will integrate with a YOLOv8 model for image analysis.
*   **Body**: `multipart/form-data` with a file.
