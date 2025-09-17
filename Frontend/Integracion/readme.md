# 🔌 Integración Frontend: JavaScript y el DOM

La integración en el frontend se refiere a cómo **HTML**, **CSS** y **JavaScript** trabajan juntos para crear una experiencia de usuario dinámica e interactiva. El rol de JavaScript es darle "vida" a la página.

---

## 🌳 El DOM (Document Object Model)

Cuando un navegador carga una página web, crea un modelo del documento en memoria. Este modelo, conocido como **DOM**, representa la estructura del documento HTML como un árbol de objetos.

*   Cada etiqueta HTML se convierte en un **objeto** en el DOM.
*   Cada atributo de una etiqueta es una **propiedad** de ese objeto.
*   JavaScript puede acceder y manipular este árbol de objetos para cambiar dinámicamente el contenido y el estilo de la página.

### ¿Qué se puede hacer con el DOM?

JavaScript puede:
*   ✅ Cambiar cualquier elemento, atributo y estilo CSS de la página.
*   ✅ Añadir o eliminar elementos y atributos.
*   ✅ Reaccionar a eventos del usuario (clics, teclas, etc.).
*   ✅ Crear nuevos eventos.

### Funciones y Propiedades Comunes del DOM

Para interactuar con el DOM, se usan métodos y propiedades del objeto `document` y de los elementos individuales.

| Método/Propiedad | Descripción |
| :--- | :--- |
| `document.getElementById('id')` | Obtiene el elemento con un ID específico. |
| `document.getElementsByTagName('p')`| Obtiene una **lista** de elementos por su etiqueta. |
| `document.getElementsByClassName('clase')`| Obtiene una **lista** de elementos por su clase. |
| `document.createElement('div')` | Crea un nuevo elemento HTML (pero no lo inserta). |
| `elemento.appendChild(hijo)` | Añade un elemento como hijo de otro. |
| `elemento.innerHTML` | Obtiene o establece el contenido HTML **dentro** de un elemento. |
| `elemento.innerText` | Obtiene o establece el contenido de texto (sin HTML) de un elemento. |
| `elemento.style` | Permite acceder y modificar los estilos CSS de un elemento. |

#### Ejemplo de uso:
```html
<!-- HTML -->
<p>Hola mundo!</p>
<p>Aguante FIUBA!</p>
```
```javascript
// JavaScript: Obtener el texto del segundo párrafo
const parrafos = document.getElementsByTagName("p");
const textoParrafo2 = parrafos[1].innerText;
console.log(textoParrafo2); // Muestra "Aguante FIUBA!" en la consola
```

---

## ⚡ Eventos: Haciendo la página interactiva

Un **evento** es una acción que ocurre en la página web, como un clic de ratón, la pulsación de una tecla o el envío de un formulario. JavaScript puede "escuchar" estos eventos y ejecutar una función en respuesta.

Para manejar un evento se necesita:
1.  Un **objeto del DOM** que "escuche" el evento (ej. un botón).
2.  Una **función** (llamada *event handler* o *listener*) que se ejecutará cuando ocurra el evento.

### Escuchando un Evento (`addEventListener`)

El método `addEventListener` es la forma moderna y recomendada de manejar eventos.

```html
<!-- HTML -->
<button id="alerta">Pulse aquí!</button>
```
```javascript
// JavaScript: Mostrar una alerta al hacer clic
const botonAlerta = document.getElementById("alerta");

botonAlerta.addEventListener("click", function(event) {
  alert("Hola mundo!");
});
```

---

## 📜 Importando Scripts en la Página

Hay dos formas de incluir código JavaScript en un documento HTML:

1.  **Interno**: Escribiendo el código directamente dentro de una etiqueta `<script>`.
2.  **Externo**: Enlazando un archivo `.js` externo mediante el atributo `src` de la etiqueta `<script>`. **(Mejor práctica)**.

> 💡 **Buena práctica**: La etiqueta `<script>` se suele colocar justo antes del cierre de la etiqueta `</body>`. Esto asegura que todo el DOM esté cargado y disponible para ser manipulado por JavaScript cuando el script se ejecute.

---
