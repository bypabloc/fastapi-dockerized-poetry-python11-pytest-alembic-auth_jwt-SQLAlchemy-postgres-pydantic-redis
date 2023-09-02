# TODO
- [x] agregar fastapi y configuracion basica de db [FastAPI, SQLAlchemy 2.0, Pydantic-V2, Alembic, Postgres and Docker](https://python.plainenglish.io/fastapi-sqlalchemy-2-0-pydantic-v2-alembic-postgres-and-docker-2c429acfc333)
- [x] agregar [middleware time](https://medium.com/@life-is-short-so-enjoy-it/fastapi-experiment-middleware-feature-c0a0c7314d74)
- [x] cambiar instancia de sqlalchemy a las rutas (Depends o Middleware)
- [x] agregar [Traefik](https://testdriven.io/blog/fastapi-docker-traefik)
- [x] agregar tests (pytest)
- [ ] agregar tasks background [celery](https://levelup.gitconnected.com/fastapi-background-tasks-vs-celery-which-is-right-for-your-application-dff0a7216e55)
- [ ] agregar auth (jwt)
- [ ] agregar sistema de roles y permisos
- [ ] agregar redis
- [ ] agregar documentacion (sphinx)
- [ ] agregar linter y formatter (evaluar los siguientes: flake8, pylint, black, autopep8)
- [ ] agregar formatter (black)
- [ ] agregar pre-commit
- [ ] agregar CI/CD (github actions)
- [ ] agregar [Beanie and MongoDB Fully Async](https://ahmed-nafies.medium.com/tutorial-fastapi-beanie-and-mongodb-fully-async-864602ca16ad)

## Levantar el proyecto en docker:
```bash
docker-compose -f docker-compose.yml up -d --build
```

## Para crear nuevas migraciones:
```bash
docker exec -it project_x_web sh -c "poetry run alembic revision --autogenerate -m 'adds user table'"
```

## Bajar el proyecto en docker:
```bash
docker-compose down -v
docker-compose -f docker-compose.prod.yml down -v
```

## Para correr el proyecto en producción:
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

## Endpoint de prueba:
```bash
http://api.localhost:8008/docs
```
