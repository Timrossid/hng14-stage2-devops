# HNG Stage 2 DevOps – Job Processor System

## Overview

This project is a simple job processing system built with:

* FastAPI (API)
* Node.js (Frontend)
* Python Worker
* Redis (Queue)
* Docker & Docker Compose

## Architecture

* **Frontend (Port 3000)** → submits jobs
* **API (Port 8000)** → handles job creation & status
* **Redis** → queue storage
* **Worker** → processes jobs asynchronously

## How to Run Locally

### 1. Clone repo

```
git clone https://github.com/Timrossid/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2. Create environment file

```
cp .env.example .env
```

### 3. Start services

```
docker compose up --build
```

### 4. Access app

* Frontend → http://localhost:3000
* API Docs → http://localhost:8000/docs

## CI/CD Pipeline

GitHub Actions pipeline includes:

* Linting (Python + ESLint + Dockerfile)
* Testing with Pytest
* Docker image build
* Security scan with Trivy
* Integration testing
* Deployment simulation

## Author

Timothy Egwuda
GitHub: https://github.com/Timrossid
