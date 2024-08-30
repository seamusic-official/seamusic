apt install python3 make docker docker-compose

if [ ! -d "backend/backend-repo" ]; then
    git clone https://github.com/username/backend-repo.git backend/backend-repo
else
    echo "Backend already was cloned"
fi

if [ ! -d "frontend/frontend-repo" ]; then
    git clone https://github.com/username/frontend-repo.git frontend/frontend-repo
else
    echo "Frontend already was cloned"
fi

cd backend/backend-repo
docker-compose -f docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
cd ../..
cd frontend/frontend-repo
docker-compose -f docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
