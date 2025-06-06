_default:
  @just --list

start-api-docker:
    docker build -f infra/Dockerfile -t namne-app .  && docker run --name namne-app --env-file ./infra/.env.development -p 8000:8000 -d namne-app

start-api:
    uvicorn server.app.main:app --reload --host 0.0.0.0 --port 8000

db-restart:
    docker stop namne-db || true
    docker rm namne-db || true
    docker build -f infra/Dockerfile.postgres -t namne-db .  && docker run --name namne-db -p 1337:1337 -d namne-db
    
dev: 