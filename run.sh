apt install python3 make docker docker-compose

if [ ! -d "backend/backend" ]; then
    git clone https://github.com/usmskolyadin/seamusic-backend.git backend/backend
else
    echo "Backend already was cloned"
fi

if [ ! -d "frontend/frontend" ]; then
    git clone https://github.com/usmskolyadin/seamusic-frontend.git frontend/frontend
else
    echo "Frontend already was cloned"
fi

cd backend/backend-repo
docker-compose -f docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
cd ../..
cd frontend/frontend-repo
docker-compose -f docker-compose.prod.yml up --force-recreate --remove-orphans --build -d
