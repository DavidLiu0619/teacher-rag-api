# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and data
COPY . .

# Set environment variables
ENV PORT=5003
ENV PYTHONUNBUFFERED=1

# Create data directory and set permissions
RUN mkdir -p /app/chroma_db && \
    chown -R nobody:nogroup /app/chroma_db

# Use non-root user
USER nobody

# Launch server
CMD ["python", "server.py"]