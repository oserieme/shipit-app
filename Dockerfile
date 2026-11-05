FROM python:3-alpine

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
LABEL org.opencontainers.image.source=https://github.com/oserieme/shipit-app.git
