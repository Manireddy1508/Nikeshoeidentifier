FROM python:3.9

WORKDIR /app

COPY . /app

COPY nike_shoe_classifier.h5 /app/nike_shoe_classifier.h5

RUN pip install -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

