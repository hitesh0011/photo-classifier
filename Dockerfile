FROM python:3.10-slim-bullseye

WORKDIR /app

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

RUN pip install --upgrade pip setuptools

RUN pip install dlib==19.22.1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]