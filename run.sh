apt install python3 make docker docker-compose
docker-compose -f backend/docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
docker-compose -f frontend/docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
