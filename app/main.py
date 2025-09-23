from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router
from .config.settings import settings  # ensures dirs are created

app = FastAPI(
    title="Face Clustering API",
    description="Upload images → Cluster by face → Download organized ZIP",
    version="1.0",
)

# Enable CORS for MERN frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "OK"}

# Only for local dev
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)