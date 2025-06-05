_default:
  @just --list

start-api:
    docker build -f infra/Dockerfile -t namne-app .  && docker run --name namne-app --env-file ./infra/.env.development -p 8000:8000 -d namne-app

start-postgres:
    docker build -f infra/Dockerfile.postgres -t namne-postgres .  && docker run --name namne-postgres -p 5432:5432 -d namne-postgres