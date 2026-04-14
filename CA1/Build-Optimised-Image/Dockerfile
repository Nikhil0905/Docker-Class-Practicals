# Stage 1
FROM python:3.11-slim AS builder
WORKDIR /app
COPY . .

# Stage 2
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /app/app.py .

CMD ["python","app.py"]