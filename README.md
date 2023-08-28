# TODO
- [ ] cambiar instancia de sqlalchemy (en rutas) por una que se llame cuando se llame el modelo
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
