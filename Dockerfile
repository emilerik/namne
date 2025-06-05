# Multi-stage Dockerfile for React + FastAPI

# Stage 1: Build React app
FROM node:18-alpine AS frontend-builder

WORKDIR /app

# Copy client package files
COPY client/package*.json ./
COPY client/pnpm-lock.yaml ./

# Install pnpm and dependencies
RUN npm install -g pnpm
RUN pnpm install

# Copy client source code
COPY client/ ./

# Build the React app
RUN pnpm run build

# Stage 2: Final image with Python and FastAPI
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy server requirements and install Python dependencies
COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy server code
COPY server/ ./

# Copy built React app from the builder stage
COPY --from=frontend-builder /app/dist /app/static

# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
