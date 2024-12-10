# Development Stage
FROM  mcr.microsoft.com/devcontainers/python:1-3.12-bookworm AS development

WORKDIR /app
COPY requirements.txt .
# Install PostgreSQL client development package
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose a port for debugging if needed
# EXPOSE 8000

CMD ["python", "main.py"]


# Production Stage
FROM python:3.12-slim AS production

WORKDIR /app
COPY --from=development /app/requirements.txt .
# Install PostgreSQL client development package
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=development /app .

CMD ["python", "main.py"]