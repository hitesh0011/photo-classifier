import face_recognition
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from pathlib import Path
from typing import List, Tuple
import shutil


def extract_face_embeddings(image_paths: List[Path]) -> Tuple[List[np.ndarray], List[Path]]:
    encodings = []
    valid_paths = []

    for path in image_paths:
        try:
            # ✅ This is what you used originally — and it worked!
            img = face_recognition.load_image_file(str(path))
            face_encodings = face_recognition.face_encodings(img)

            if face_encodings:
                encodings.append(face_encodings[0])
                valid_paths.append(path)

        except Exception as e:
            print(f"⚠️ Skipping {path.name}: {str(e)}")
            continue  # Skip bad/unreadable images

    return encodings, valid_paths


def cluster_faces(encodings: List[np.ndarray]) -> np.ndarray:
    clustering = DBSCAN(eps=0.46, min_samples=2, metric="euclidean").fit(encodings)
    return clustering.labels_


def group_images_by_cluster(valid_paths: List[Path], labels: np.ndarray, output_dir: Path):
    for path, label in zip(valid_paths, labels):
        person_folder = output_dir / f"person_{label}"
        person_folder.mkdir(exist_ok=True)
        shutil.copy(path, person_folder / path.name)
