#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Name Voting App - Docker Compose Setup${NC}"
echo "======================================"

# Check if .env file exists in parent directory
if [ ! -f ../.env ]; then
    echo -e "${YELLOW}No .env file found in parent directory. Creating from template...${NC}"
    
    # Create .env with default values in parent directory
    cat > ../.env << EOF
# Security
SECRET_KEY=dev-secret-key-$(openssl rand -hex 32)

# CORS Settings
CORS_ORIGINS=http://localhost:8000,http://localhost:3000

# PostgreSQL Settings
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppassword
POSTGRES_DB=appdb

# App Settings
APP_PORT=8000
EOF
    
    echo -e "${GREEN}.env file created in parent directory with default values${NC}"
    echo -e "${YELLOW}⚠️  Please update SECRET_KEY for production use!${NC}"
fi

# Parse command line arguments
case "$1" in
    "up")
        echo -e "${GREEN}Starting services...${NC}"
        docker-compose up --build
        ;;
    "up-d")
        echo -e "${GREEN}Starting services in detached mode...${NC}"
        docker-compose up -d --build
        ;;
    "down")
        echo -e "${YELLOW}Stopping services...${NC}"
        docker-compose down
        ;;
    "logs")
        docker-compose logs -f
        ;;
    "clean")
        echo -e "${RED}⚠️  This will delete all data including the database!${NC}"
        read -p "Are you sure? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            docker-compose down -v
            echo -e "${GREEN}All containers and volumes removed${NC}"
        fi
        ;;
    "prod")
        echo -e "${GREEN}Starting production configuration...${NC}"
        docker-compose -f docker-compose.prod.yml up -d --build
        ;;
    *)
        echo "Usage: $0 {up|up-d|down|logs|clean|prod}"
        echo ""
        echo "Commands:"
        echo "  up      - Start all services (attached)"
        echo "  up-d    - Start all services (detached)"
        echo "  down    - Stop all services"
        echo "  logs    - Follow logs from all services"
        echo "  clean   - Stop services and remove all data"
        echo "  prod    - Start with production configuration"
        echo ""
        echo "Note: Run this script from the infra/ directory"
        echo "The .env file will be created in the parent directory if it doesn't exist"
        exit 1
        ;;
esac 