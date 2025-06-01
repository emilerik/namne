# Docker Setup for Name Voting App

This project uses Docker Compose to run:

- PostgreSQL database (separate container)
- FastAPI backend server with React frontend (served as static files)

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. **Navigate to the infra directory:**

   ```bash
   cd infra
   ```

2. **Build and run the containers using the helper script:**

   ```bash
   ./run.sh up
   ```

   Or run in detached mode:

   ```bash
   ./run.sh up-d
   ```

   **Alternative: Using docker-compose directly:**

   ```bash
   docker-compose up --build
   ```

## Access the Application

- **Frontend**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/api/health
- **PostgreSQL**: localhost:5432 (if you need direct database access)

## Common Commands

### Using the helper script (recommended)

```bash
cd infra

# Start services
./run.sh up

# Start in detached mode
./run.sh up-d

# View logs
./run.sh logs

# Stop services
./run.sh down

# Clean everything (removes data!)
./run.sh clean

# Production mode
./run.sh prod
```

### Using docker-compose directly

```bash
cd infra

# View logs
docker-compose logs

# Specific service
docker-compose logs app
docker-compose logs postgres

# Follow logs
docker-compose logs -f app

# Stop services
docker-compose down

# Stop and remove volumes (WARNING: This deletes the database!)
docker-compose down -v

# Rebuild after code changes
docker-compose build app
docker-compose up -d

# Access the app container
docker-compose exec app bash

# Access PostgreSQL
docker-compose exec postgres psql -U appuser -d appdb
```

## Configuration

### Environment Variables

The system will automatically create a `.env` file in the project root (parent directory) with default values if it doesn't exist. You can customize these values:

```env
# Security
SECRET_KEY=your-very-secure-secret-key

# CORS Settings
CORS_ORIGINS=http://localhost:8000,https://yourdomain.com

# PostgreSQL Settings (for production)
POSTGRES_USER=appuser
POSTGRES_PASSWORD=your-secure-password
POSTGRES_DB=appdb

# App Settings
APP_PORT=8000
```

## Database Information

The PostgreSQL database is configured with:

- Database: `appdb`
- User: `appuser`
- Password: `apppassword` (default, change via .env)
- Host (from app container): `postgres`
- Host (from host machine): `localhost`
- Port: `5432`

## Data Persistence

- PostgreSQL data is persisted in a Docker volume named `postgres_data`
- Application data files are optionally mounted from `../server/data`

## Project Structure

```
namne/
├── infra/                    # Docker infrastructure
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.prod.yml
│   ├── run.sh
│   └── DOCKER_README.md
├── client/                   # React frontend
├── server/                   # FastAPI backend
├── .env                     # Environment variables (auto-created)
└── .dockerignore            # Docker ignore file
```

## Production Considerations

For production deployment:

1. Use strong passwords and secrets in your `.env` file
2. Configure CORS_ORIGINS appropriately
3. Consider using Docker secrets for sensitive data
4. Set up proper logging and monitoring
5. Use a reverse proxy (nginx, traefik) for SSL/TLS
6. Regular database backups

## Troubleshooting

### Database connection issues

1. Ensure PostgreSQL is healthy: `docker-compose ps`
2. Check if the database was initialized: `docker-compose logs app | grep "Database initialized"`
3. Verify environment variables: `docker-compose exec app env | grep DATABASE`

### Port conflicts

If port 8000 or 5432 is already in use, modify the ports in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000" # Change 8001 to your desired port
```

### Build context issues

The Docker build context is set to the parent directory (`..`) to access both client and server code. Make sure to run docker-compose from the `infra/` directory.
