apt install python3 make docker docker-compose
python -m docker-compose -f backend/docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
python -m docker-compose -f frontend/docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
