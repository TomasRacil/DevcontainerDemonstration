FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm AS development
CMD [ "python", "main.py" ]

FROM python:3 AS production

WORKDIR /backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 8000/tcp

CMD [ "python", "main.py" ]