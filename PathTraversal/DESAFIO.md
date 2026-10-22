# Hidden Flag

## 1. Descripción del desafío

- **Categoría:** Web
- **Dificultad:** Fácil / intermedia
- **Tecnologías:** Python, Flask, HTML y CSS
- **Vulnerabilidad:** Path Traversal
- **Cifrado final:** ROT13 (César 13)

## Enunciado para participantes

> El archivo de incidentes menciona que la rotación de backups quedó pendiente. El índice público no siempre cuenta toda la historia. Encontrá el registro perdido y recuperá el token.

## Pistas

1. **Reconocimiento:** revisá `robots.txt` y las rutas mencionadas allí.
2. **Parámetros:** la descarga recibe el nombre del archivo mediante el parámetro `file`.
3. **Traversal:** probá navegar al directorio padre con `../`.
4. **Codificación:** el token recuperado está en ROT13.