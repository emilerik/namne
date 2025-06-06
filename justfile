_default:
  @just --list

start-api-docker:
    docker stop namne-app || true
    docker rm namne-app || true
    docker build -f Dockerfile -t namne-app .  && docker run --name namne-app --env-file ./infra/.env.local-docker -p 8080:8080 -d namne-app

start-api:
    uvicorn server.app.main:app --reload --host 0.0.0.0 --port 8080

start-client:
    npx dotenv -e .env.development -- pnpm --dir client dev

db-restart:
    docker stop namne-db || true
    docker rm namne-db || true
    docker build -f infra/Dockerfile.postgres -t namne-db .  && docker run --name namne-db -p 1337:1337 -d namne-db