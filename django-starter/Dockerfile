FROM python:3.12-slim-bookworm AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo libwebp7 && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -m wagtail
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY . .
ENV PYTHONUNBUFFERED=1
USER wagtail
EXPOSE 8000
CMD ["gunicorn", "_core.wsgi:application", "--bind", "0.0.0.0:8000"]