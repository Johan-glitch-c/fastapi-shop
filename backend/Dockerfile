FROM python:3.11-slim


WORKDIR /app

RUN apt-get update && apt-get install \
    gcc \
    && rm -rf /var/lib/apt/lists/*


COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN mkdir -p static/images

RUN chmod -R 755 static

EXPOSE 8000

CMD ["uvicorn", "app.main.py", "--host", "0.0.0.0", "--port", "8000"]