FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Separate apt-get update to allow better caching and debugging
RUN apt-get update

# Split install into two blocks to isolate slow installs
RUN apt-get install -y --no-install-recommends \
    build-essential \
    libpango-1.0-0 \
    libcairo2 \
    libpangocairo-1.0-0

RUN apt-get install -y --no-install-recommends \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libxml2 \
    libxslt1.1 \
    zlib1g-dev \
    libjpeg-dev \
    shared-mime-info \
    curl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "invoice_generator.wsgi:application"]
