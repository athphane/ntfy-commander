# Stage 1: Copy the binary from the ntfy container
FROM binwiederhier/ntfy AS ntfy_source

# Stage 2: Create the final image based on the official Python 3.11 image
FROM python:3.11-slim

LABEL maintainer="Athfan Khaleel <athphane@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/athphane/ntfy-commander"
LABEL org.opencontainers.image.documentation="https://github.com/athphane/ntfy-commander/wiki"
LABEL org.opencontainers.image.description="A docker image with ntfy and a webui to help administer it"

# Install necessary packages
RUN apt-get update && apt-get install -y \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy the ntfy binary from the ntfy container
COPY --from=ntfy_source /usr/bin/ntfy /usr/bin/ntfy

# Set up a working directory
WORKDIR /server

# Copy requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /server/requirements.txt

# Copy application code
COPY server /server

# Create a directory for supervisor configuration files
RUN mkdir -p /etc/supervisor/conf.d

# Copy the supervisord.conf file
COPY build/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the port on which your FastAPI app will run (default 8000)
EXPOSE 80 8000

# Command to run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
