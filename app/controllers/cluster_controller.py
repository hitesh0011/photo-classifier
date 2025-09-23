# app/controllers/cluster_controller.py

import shutil
from fastapi import UploadFile, HTTPException
from pathlib import Path
from typing import List
from ..config.settings import settings
from ..services.face_clustering import extract_face_embeddings, cluster_faces, group_images_by_cluster
from ..utils.file_utils import clean_directory, create_zip_from_directory


async def handle_cluster_and_zip(files: List[UploadFile]) -> Path:
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    # Clean temp directories
    clean_directory(settings.UPLOAD_DIR)
    clean_directory(settings.CLUSTER_DIR)

    # Save uploaded files — no format validation needed
    image_paths: List[Path] = []
    for file in files:
        file_path = settings.UPLOAD_DIR / file.filename
        contents = await file.read()
        with open(file_path, "wb") as buffer:
            buffer.write(contents)
        image_paths.append(file_path)

    # Extract embeddings — uses same logic as original script
    encodings, valid_paths = extract_face_embeddings(image_paths)

    if len(encodings) == 0:
        raise HTTPException(status_code=400, detail="No faces detected in any image")

    # Cluster
    labels = cluster_faces(encodings)

    # Group into folders
    group_images_by_cluster(valid_paths, labels, settings.CLUSTER_DIR)

    # Create ZIP
    zip_path = create_zip_from_directory(settings.CLUSTER_DIR)

    return zip_path