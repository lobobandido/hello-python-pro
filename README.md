# Hello Python Pro

**Proyecto:** API ejemplo con FastAPI + SQLModel (SQLite)  
**Propósito:** Repositorio para practicar backend Python, CRUD, CI, tests y buenas prácticas.  
**Autor:** Adolfo Antonio (lobobandido)

---

## Estado
- FastAPI + Uvicorn
- SQLModel (SQLite)
- Pre-commit (black, isort, ruff, mypy)
- Tests con `pytest`
- Estructura modular (app/core, app/db, app/models, app/schemas, app/routes, app/crud)

---

## Requisitos locales
- Python 3.11+ instalado
- Poetry instalado

---

## Instalación (local)
```bash
cd hello-python-pro
poetry install
cp .env.example .env   # editar si es necesario
