FROM python:3.8

RUN apt-get update -y && apt-get install gdal-bin ffmpeg -y

COPY requirements.* ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app

RUN chown -R 1000:1000 /app

EXPOSE 8000

WORKDIR /app

CMD sleep infinity