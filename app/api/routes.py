from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from typing import Annotated
from ..controllers.cluster_controller import handle_cluster_and_zip

router = APIRouter(prefix="/api/v1", tags=["Clustering"])

@router.post("/cluster-and-zip")
async def cluster_and_zip_endpoint(
    files: Annotated[
        list[UploadFile],
        File(description="Select multiple image files (JPG/PNG) to cluster by detected faces")
    ]
):
    """
    Upload multiple images → system detects faces → clusters them → returns ZIP with folders.
    """
    zip_path = await handle_cluster_and_zip(files)

    return FileResponse(
        path=zip_path,
        filename=zip_path.name,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename={zip_path.name}"}
    )