# Hidden Flag (CTF Web)

## Requisitos

- Python 3.10+ (recomendado 3.12)
- pip

## Ejecutar localmente

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Abrí http://127.0.0.1:5000

## Ejecutar con Docker

```bash
docker compose up --build
```

Abrí http://127.0.0.1:5000. El puerto queda publicado solo en `127.0.0.1`.

