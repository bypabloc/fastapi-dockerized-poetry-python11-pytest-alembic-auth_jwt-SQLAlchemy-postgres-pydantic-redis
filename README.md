# TODO
- [ ] agregar fastapi y configuracion basica de db [FastAPI, SQLAlchemy 2.0, Pydantic-V2, Alembic, Postgres and Docker](https://python.plainenglish.io/fastapi-sqlalchemy-2-0-pydantic-v2-alembic-postgres-and-docker-2c429acfc333)
- [x] agregar [middleware time](https://medium.com/@life-is-short-so-enjoy-it/fastapi-experiment-middleware-feature-c0a0c7314d74)
- [ ] agregar tasks background [celery](https://levelup.gitconnected.com/fastapi-background-tasks-vs-celery-which-is-right-for-your-application-dff0a7216e55)
- [ ] cambiar instancia de sqlalchemy a las rutas (Depends o Middleware)
- [ ] agregar [Traefik](https://testdriven.io/blog/fastapi-docker-traefik)
- [ ] agregar tests (pytest)
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
docker-compose up -d --build
```

## Para crear nuevas migraciones:
```bash
docker exec -it project_x_web sh -c "poetry run alembic revision --autogenerate -m 'adds user table'"
```
