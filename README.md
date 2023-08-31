# TODO
- [ ] agregar [middleware time](https://medium.com/@life-is-short-so-enjoy-it/fastapi-experiment-middleware-feature-c0a0c7314d74)
- [ ] agregar tasks background [celery](https://levelup.gitconnected.com/fastapi-background-tasks-vs-celery-which-is-right-for-your-application-dff0a7216e55)
- [ ] cambiar instancia de sqlalchemy a las rutas (Depends o Middleware)
- [ ] agregar [traefik](https://testdriven.io/blog/fastapi-docker-traefik/)
- [ ] agregar tests (pytest)
- [ ] agregar auth (jwt)
- [ ] agregar sistema de roles y permisos
- [ ] agregar redis
- [ ] agregar documentacion (sphinx)
- [ ] agregar linter y formatter (evaluar los siguientes: flake8, pylint, black, autopep8)
- [ ] agregar formatter (black)
- [ ] agregar pre-commit
- [ ] agregar CI/CD (github actions)

## Levantar el proyecto en docker:
```bash
docker-compose up -d --build
```

## Para crear nuevas migraciones:
```bash
docker exec -it project_x_web sh -c "poetry run alembic revision --autogenerate -m 'adds user table'"
```
