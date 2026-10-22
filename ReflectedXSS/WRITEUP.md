# WriteUp CTF: Reflected XSS

## 1. Exploré la página principal

Ingresé a la página web y encontré un formulario de verificación de visitantes.

La página solicitaba un nombre y mostraba un saludo personalizado después de enviar el formulario.

Esto me llevó a investigar si el valor introducido se utilizaba únicamente como texto o si la aplicación lo incorporaba directamente al código HTML.

## 2. Analicé el parámetro de entrada

Observé que el formulario utilizaba el método GET y enviaba el nombre mediante el parámetro `name`.

Por ejemplo:

```text
http://127.0.0.1:5000/?name=Eduardo
```

Al enviar un nombre normal, la página mostraba el saludo correspondiente.

Esto indicaba que la aplicación recibía el valor del parámetro y lo utilizaba para generar la respuesta HTML.

## 3. Investigué si la entrada se interpretaba como HTML

Para comprobar cómo se procesaba el parámetro, introduje una etiqueta HTML en el campo del nombre.

Utilicé la siguiente prueba de concepto:

```html
<script>alert('XSS')</script>
```

Al enviar el formulario, el navegador ejecutó el código JavaScript.

Esto demostró que la aplicación no estaba escapando correctamente la entrada del usuario antes de incorporarla al HTML.

## 4. Identifiqué la vulnerabilidad XSS reflejada

Revisé el código de la plantilla `templates/index.html` y encontré la siguiente línea:

```html
<div id="greeting">Bienvenido: {{ name | safe }}</div>
```

El parámetro `name` se incorporaba a la página mediante el filtro `safe` de Jinja.

Este filtro indica a la plantilla que debe tratar el contenido como HTML seguro, evitando el escape automático que normalmente protege frente a la interpretación de etiquetas introducidas por el usuario.

Como consecuencia, un atacante puede introducir contenido HTML y JavaScript que el navegador interpreta al cargar la respuesta.

Esta vulnerabilidad se conoce como **Cross-Site Scripting reflejado (Reflected XSS)**, porque la entrada enviada mediante una petición se devuelve en la respuesta de la aplicación y puede ejecutarse en el navegador.

## 5. Investigué cómo recuperar la flag

Después de confirmar la ejecución de JavaScript, analicé el código de la página y encontré que la aplicación definía la siguiente variable:

```javascript
window.FLAG
```

La variable contenía la flag del desafío.

Para recuperarla, utilicé esta prueba de concepto:

```html
<script>alert(window.FLAG)</script>
```

Al introducirla en el parámetro `name`, el navegador ejecutó el JavaScript y mostró el contenido de la variable en una ventana emergente.

## 6. Recuperé la flag final

La flag obtenida fue:

```text
flag{reflected_xss_grupo3}
```

Con esto completé el desafío.

## 7. Conclusión

Para resolver este CTF, primero exploré el formulario de verificación y analicé el parámetro `name`. Después, comprobé que la aplicación interpretaba una etiqueta HTML introducida por el usuario y ejecutaba JavaScript.

Al revisar la plantilla, identifiqué el uso del filtro `safe`, que impedía el escape automático del contenido. Esto permitió explotar una vulnerabilidad XSS reflejada.

Finalmente, utilicé la ejecución de JavaScript para leer la variable `window.FLAG` y recuperar la flag del desafío.