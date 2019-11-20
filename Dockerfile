FROM python:3.7-buster
COPY src/ ./
COPY tests/ ./tests
ENTRYPOINT ["python", "main.py"]
