# Name Voting App

A full-stack application for voting on baby names, built with React frontend and FastAPI backend.

## Project Structure

```
namne/
├── infra/                    # 🐳 Docker infrastructure & deployment
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.prod.yml
│   ├── run.sh
│   └── DOCKER_README.md     # 📖 Docker setup instructions
├── client/                   # ⚛️ React frontend (Vite + TypeScript)
├── server/                   # 🐍 FastAPI backend
├── .env                     # 🔧 Environment variables (auto-created)
└── .dockerignore
```

## Quick Start with Docker

The easiest way to run the entire application:

```bash
cd infra
./run.sh up
```

Then visit: http://localhost:8000

For detailed Docker setup instructions, see [`infra/DOCKER_README.md`](infra/DOCKER_README.md)

## Development Setup

### Backend (FastAPI)

```bash
cd server
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (React)

```bash
cd client
pnpm install
pnpm dev
```

## Features

- 🗳️ Vote on baby names (like, dislike, superlike)
- 💖 Match detection when both partners like the same name
- 🔐 Basic authentication
- 📱 Responsive modern UI
- 🐳 Containerized deployment
- 🗄️ PostgreSQL database

## Tech Stack

- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Deployment**: Docker, Docker Compose
- **Auth**: HTTP Basic Authentication

## API Endpoints

All API endpoints are prefixed with `/api/`:

- `GET /api/health` - Health check
- `GET /api/names` - Get names for voting
- `POST /api/name/{id}` - Vote on a name
- `GET /api/authenticate` - Check authentication

API documentation available at: http://localhost:8000/docs

## License

MIT
