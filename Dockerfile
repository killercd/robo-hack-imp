FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

RUN python init_db.py
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
