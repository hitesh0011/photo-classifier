from pathlib import Path

class Settings:
    UPLOAD_DIR: Path = Path("uploads")
    CLUSTER_DIR: Path = Path("clusters")

    def __init__(self):
        self.UPLOAD_DIR.mkdir(exist_ok=True)
        self.CLUSTER_DIR.mkdir(exist_ok=True)

    
settings = Settings()