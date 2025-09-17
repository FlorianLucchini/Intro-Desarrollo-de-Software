# Apuntes de Frontend 🎨

El Frontend es la parte de una aplicación que interactúa directamente con el usuario. Comprende la interfaz de usuario (UI), el diseño y la experiencia de usuario (UX). Se construye principalmente con la tríada: **HTML**, **CSS** y **JavaScript**.

---

## 🧱 HTML (HyperText Markup Language)

HTML es el lenguaje de marcado estándar para crear la **estructura** y el **contenido** de las páginas web.

### Etiquetas (`Tags`)

Las etiquetas son los bloques de construcción de HTML. Definen cómo se formatea y se muestra el contenido.

#### Etiquetas Básicas

| Etiqueta | Descripción |
| :--- | :--- |
| `<!DOCTYPE html>` | Define el tipo de documento. Es una buena práctica incluirlo siempre. |
| `<html>` | Etiqueta raíz que engloba todo el contenido. |
| `<head>` | Contiene metadatos, títulos y enlaces a CSS/scripts. No es visible en la página. |
| `<body>` | Contiene todo el contenido visible de la página. |
| `<h1>` a `<h6>` | Títulos y subtítulos, ordenados por importancia. |
| `<p>` | Párrafos de texto. |
| `<div>` | Contenedor genérico para agrupar y estilizar elementos. |
| `<a>` | Enlaces (hipervínculos). |
| `<img>` | Incrustar imágenes. |
| `<form>`, `<input>` | Creación de formularios para la entrada de datos del usuario. |

### Atributos

Los atributos proporcionan información adicional sobre un elemento HTML y se especifican siempre en la etiqueta de apertura.

| Atributo | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `id` | Identificador **único** para un elemento. | `<div id="header">` |
| `class` | Identificador **no único** para aplicar estilos a múltiples elementos. | `<p class="texto-destacado">` |
| `href` | URL de destino para un enlace. | `<a href="https://google.com">` |
| `src` | Ruta (URL) del recurso a incrustar (ej. una imagen). | `<img src="./images/logo.png">` |

### Ejemplo de Página Web Básica

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Página Web</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 class="titulo">Pala Store: PCs a tu medida</h1>
    <div id="productos">
        <h2>Nuestros productos</h2>
        <ul id="lista-componentes">
            <li>Procesador Ryzen 9</li>
            <li>Placa de video Nvidia RTX 4090</li>
        </ul>
    </div>
</body>
</html>
```

---

## 🎨 CSS (Cascading Style Sheets)

CSS es el lenguaje utilizado para describir la **presentación** y el **diseño visual** de un documento HTML.

### Estructura Básica de una Regla CSS

*   **Selector**: Apunta al elemento HTML que quieres estilizar.
*   **Declaración**: Compuesta por una propiedad y un valor, define el estilo a aplicar.

### Selectores

Indican a qué elementos se les aplicará un estilo.

| Tipo de Selector | Sintaxis | Descripción |
| :--- | :--- | :--- |
| Por Etiqueta/Tipo | `p`, `h1`, `div` | Selecciona todos los elementos de un tipo. |
| Por Clase | `.nombre-clase` | Selecciona todos los elementos con esa clase. |
| Por ID | `#nombre-id` | Selecciona el único elemento con ese ID. |
| Por Atributo | `[type="text"]` | Selecciona elementos con un atributo específico. |
| Universal | `*` | Selecciona **todos** los elementos. |

> **Diferencia clave:** `id` es para un único elemento, `class` es para agrupar y estilizar a muchos.

### Formas de Insertar CSS

1.  **En línea (Inline)**: Usando el atributo `style` directamente en la etiqueta HTML. (No recomendado para sitios grandes).
    ```html
    <h1 style="color: red;">Hola Mundo</h1>
    ```
2.  **Interno (Internal)**: Usando la etiqueta `<style>` dentro del `<head>` del HTML.
    ```html
    <head>
        <style>
            h1 {
                color: blue;
            }
        </style>
    </head>
    ```
3.  **Externo (External)**: Enlazando un archivo `.css` separado usando la etiqueta `<link>` en el `<head>`. **(Mejor práctica)**.
    ```html
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    ```

### Buenas Prácticas en CSS

*   **Organización**: Estilizar desde los elementos más generales (contenedores grandes) a los más específicos (botones, texto).
*   **Especificidad**: Tener en cuenta que los estilos se "pisan" o sobreescriben. Un selector más específico (como un `id`) tiene más peso que uno general (como una etiqueta).
*   **Indentación**: Mantener el código ordenado y legible.

---

## ⚙️ Integración con Flask (Templates)

Flask utiliza el motor de plantillas **Jinja2**, que permite integrar lógica de Python directamente en los archivos HTML.

### Variables y Estructuras de Control

Puedes pasar variables desde tu aplicación Flask al template y mostrarlas usando `{{ ... }}`. También puedes usar estructuras de control como `if` y `for` dentro de bloques `{% ... %}`.

*   **Variables**: `{{ mi_variable }}`
*   **Bucles `for`**:
    ```html
    <ul>
    {% for comentario in comentarios %}
        <li>{{ comentario }}</li>
    {% endfor %}
    </ul>
    ```

*   **Condicionales `if`**:
    ```html
    {% if user %}
        <p>Hola, {{ user }}!</p>
    {% else %}
        <p>Hola, Invitado!</p>
    {% endif %}
    ```

### Enlaces y Archivos Estáticos (`url_for`)

Para cargar archivos estáticos (CSS, JS, imágenes) o generar enlaces a otras rutas de tu aplicación, es una buena práctica usar la función `url_for()`. Esto evita romper los enlaces si cambias las URLs de tus rutas.

*   **Cargar CSS**:
    ```html
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/style.css') }}">
    ```
*   **Cargar Imágenes**:
    ```css
    body {
        background-image: url("{{ url_for('static', filename='images/background.jpg') }}");
    }
    ```

---
