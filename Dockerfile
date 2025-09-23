# Dockerfile — Fixed for dlib + FastAPI + Render/Cloud Run

FROM python:3.10-slim-bullseye

WORKDIR /app

# 1. Install system deps (including system cmake, not pip cmake)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    libjpeg-dev \
    libswscale-dev \
    libavcodec-dev \
    libavformat-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip + setuptools (as guide suggests)
RUN pip install --upgrade pip setuptools

# 3. Install dlib FIRST — force a version with fixed pybind11
#    dlib 19.22.1 has known good pybind11 compatibility
RUN pip install dlib==19.22.1

# 4. Now install your other requirements (face_recognition will skip installing dlib)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your app code
COPY . .

# 6. Expose port
EXPOSE 8000

# 7. Start FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]