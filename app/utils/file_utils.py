import shutil
from pathlib import Path
import zipfile
import uuid


def clean_directory(dir_path: Path):
    # for deleting the temp foldders after there use
    for item in dir_path.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

    
def create_zip_from_directory(source_dir: Path) -> Path:
    # to create a zip file
    zip_filename = f"clusters_{uuid.uuid4().hex}.zip"
    zip_path = source_dir.parent / zip_filename

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for folder in source_dir.iterdir():
            if folder.is_dir():
                for file in folder.iterdir():
                    zipf.write(file, arcname = f"{folder.name}/{file.name}")

    return zip_path
