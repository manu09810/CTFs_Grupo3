# Reflected XSS (CTF Web)

## 1. Requisitos

- Windows, Linux o macOS.
- Python 3.10 o superior; se recomienda Python 3.12.
- pip para instalar las dependencias.
- Un navegador web moderno.

El proyecto utiliza Flask y no necesita una base de datos.

## 2. Estructura del proyecto

```text
ReflectedXSS/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 3. Ejecutar localmente en Windows

Abrí PowerShell dentro de la carpeta `ReflectedXSS`.

### Crear el entorno virtual

```powershell
python -m venv .venv
```

### Instalar las dependencias

No es necesario activar el entorno virtual. Para evitar problemas con las políticas de ejecución de PowerShell, ejecutá directamente el Python del entorno:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Iniciar el servidor

```powershell
.\.venv\Scripts\python.exe app.py
```

El servidor quedará disponible en:

http://127.0.0.1:5000

## 4. Ejecutar localmente en Linux/macOS

Desde la carpeta del proyecto, ejecutá:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Abrí http://127.0.0.1:5000 en el navegador.

## 5. Solución de problemas

### PowerShell bloquea Activate.ps1

No es necesario activar el entorno. Utilizá directamente:

```powershell
.\.venv\Scripts\python.exe app.py
```

### Flask no está instalado

Ejecutá:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### El puerto 5000 está ocupado

Cerrá el proceso que esté utilizando ese puerto o cambiá el puerto configurado en `app.py`.

### No se ejecuta el JavaScript

Comprobá que estés utilizando el parámetro `name` y que el navegador permita ejecutar JavaScript.

