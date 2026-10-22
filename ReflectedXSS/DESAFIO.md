
# Reflected XSS

## 1. Descripción del desafío

- **Categoría:** Web
- **Dificultad:** Fácil / intermedia
- **Tecnologías:** Python, Flask, HTML y CSS
- **Vulnerabilidad:** Cross-Site Scripting (XSS) reflejado
- **Objetivo:** Ejecutar JavaScript mediante una entrada controlada y recuperar la flag.

## Enunciado para participantes

> Se utiliza un sistema de verificación de visitantes que genera un saludo personalizado. Sin embargo, algunos usuarios sospechan que el sistema procesa incorrectamente los datos introducidos.

## 2. Pistas 

1. **Reconocimiento:** observá cómo cambia la página cuando enviás un nombre.
2. **Parámetros:** investigá el parámetro `name` de la URL.
3. **HTML:** comprobá si la aplicación interpreta etiquetas HTML introducidas por el usuario.
4. **JavaScript:** investigá si es posible ejecutar código JavaScript desde el saludo personalizado.
5. **Flag:** revisá qué información está disponible en el contexto JavaScript de la página.
