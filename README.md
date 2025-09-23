# Photo Classifier

A FastAPI-powered backend for face clustering and bulk photo organization. Upload multiple images, and the system automatically detects faces, clusters them by similarity, and returns a downloadable ZIP archive with organized folders—each folder representing a unique person.

---

## Features

- **Face Clustering**: Uses state-of-the-art face recognition and clustering (DBSCAN) to group photos by detected individuals.
- **Bulk Upload & Organization**: Upload multiple images (JPG/PNG) at once. Instantly receive a ZIP archive with folders for each detected person.
- **REST API**: FastAPI backend with a `/cluster-and-zip` endpoint for seamless integration with frontends (MERN or others).
- **Docker Support**: Includes a ready-to-use Dockerfile for containerized deployment.
- **Cross-Origin Resource Sharing (CORS)**: Enabled for easy connection to web frontends.

---

## How It Works

1. **Upload Images**: Send a POST request to `/api/v1/cluster-and-zip` with multiple image files.
2. **Face Embedding Extraction**: Each image is processed to extract facial embeddings using `face_recognition`.
3. **Clustering**: Embeddings are clustered using DBSCAN, grouping similar faces together.
4. **Organization**: Images are sorted into folders—one per cluster (i.e., per unique person).
5. **Download ZIP**: Receive a ZIP archive containing folders (e.g., `person_0`, `person_1`, ...) with the corresponding images.

---

## API Usage

### Endpoint

```
POST /api/v1/cluster-and-zip
```

#### Request

- **Content-Type**: `multipart/form-data`
- **Body**: One or more image files (JPG/PNG)

#### Response

- **Status**: `200 OK`
- **Body**: ZIP file containing folders of clustered images

---

## Local Development

### Requirements

#### For Ubuntu/Linux

Install these system packages first (needed for `face_recognition` and other deep learning libraries):

```sh
sudo apt-get update
sudo apt-get install build-essential cmake libgtk-3-dev libboost-python-dev
```

#### For Windows

- **CMake**: Download and install [CMake for Windows](https://cmake.org/download/).
- **Visual Studio Build Tools**:  
  Download and install [Build Tools for Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/).  
  - During installation, select the "C++ build tools" workload.
- **Python and pip**: Download and install Python 3.10+ and pip from [python.org](https://www.python.org/downloads/).
- **Restart your terminal after installation** to make sure the new tools are available in your PATH.

> **Note:**  
> Windows users do not need `libgtk-3-dev` or `libboost-python-dev`; those are Linux-only dependencies.

#### Python Dependencies

- Create a virtual environment (recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Run Locally

```
uvicorn app.main:app --reload
```

- The health check endpoint `/` returns `{ "status": "OK" }`

### Docker

Build and run with Docker (no need to install system dependencies manually):

```
docker build -t photo-classifier .
docker run -p 8000:8000 photo-classifier
```

---

## File & Directory Structure

- `app/main.py`: FastAPI app setup and entrypoint
- `app/api/routes.py`: API route for clustering and downloading ZIP
- `app/controllers/cluster_controller.py`: Orchestrates upload handling, clustering, and zipping
- `app/services/face_clustering.py`: Face embedding extraction, clustering, folder organization
- `app/utils/file_utils.py`: File and ZIP management utilities
- `app/config/settings.py`: Directory setup/configuration

---

## Example Request (Python)

```python
import requests

files = [
    ('files', open('photo1.jpg', 'rb')),
    ('files', open('photo2.jpg', 'rb')),
    # ...add more files
]

response = requests.post('http://localhost:8000/api/v1/cluster-and-zip', files=files)

with open('clusters.zip', 'wb') as f:
    f.write(response.content)
```

---

## Contributing

Contributions and suggestions are welcome! Please open issues or pull requests.

---

## License

[MIT](LICENSE)

---

## Author

- [hitesh0011](https://github.com/hitesh0011)
