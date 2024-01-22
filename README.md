# Исходный код для Y_lab University


## Описание проекта


## Используемый стэк:

  python3.9, FastAPI, Postgresql

### Клонировать репозиторий

```sh
git clone https://github.com/morley-d/y_lab_fapi_project.git
```

### Установка зависимостей
```shell
pip install -r requirements.txt
```

### Roll up migrations

```sh
alembic upgrade head
```

### Run app

```sh
uvicorn app.main:app --reload
```
