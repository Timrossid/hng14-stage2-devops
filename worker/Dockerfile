FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python healthcheck.py

CMD ["python", "worker.py"]