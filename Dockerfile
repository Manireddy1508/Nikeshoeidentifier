FROM python:3.9

WORKDIR /app

COPY nike_shoe_classifier.h5 /app/nike_shoe_classifier.h5

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

