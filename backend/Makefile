DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
BACKEND_FILE = docker-compose.yml
BACKEND_CONTAINER = my_app


.PHONY: backend
backend:
	${DC} -f ${BACKEND_FILE} ${ENV} up --build -d

.PHONY: backend-logs
backend-logs:
	${LOGS} ${BACKEND_CONTAINER} -f

.PHONY: backend-down
backend-down:
	${DC} -f ${BACKEND_FILE} down


