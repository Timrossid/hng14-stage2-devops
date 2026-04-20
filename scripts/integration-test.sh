#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  docker compose down -v
}
trap cleanup EXIT

echo "Starting services..."
docker compose up -d --build

echo "Waiting for services..."
timeout 60 bash -c '
  until curl -fsS http://localhost:3000 >/dev/null; do sleep 2; done
  until curl -fsS http://localhost:8000/health >/dev/null; do sleep 2; done
'

echo "Submitting job..."
JOB_ID=$(curl -fsS -X POST http://localhost:3000/submit | python -c "import sys, json; print(json.load(sys.stdin)[\"job_id\"])")

echo "Job ID: $JOB_ID"

echo "Checking job status..."
timeout 60 bash -c "
  while true; do
    STATUS=\$(curl -fsS http://localhost:8000/jobs/$JOB_ID | python -c 'import sys, json; print(json.load(sys.stdin).get(\"status\",\"\"))')
    echo Status: \$STATUS
    if [ \"\$STATUS\" = \"completed\" ]; then
      exit 0
    fi
    sleep 2
  done
"

echo "Integration test passed"