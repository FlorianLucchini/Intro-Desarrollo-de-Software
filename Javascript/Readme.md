# 📜 Apuntes de JavaScript

JavaScript es un lenguaje de programación que permite añadir interactividad y dinamismo a las páginas web. En el contexto de este curso, es importante diferenciar:
1.  **JavaScript**: El lenguaje en sí.
2.  **ECMAScript**: El estándar que define cómo debe ser el lenguaje. JavaScript es una implementación de este estándar.
3.  **TypeScript**: Un superset de JavaScript que añade tipado estático y otras características avanzadas.

---

## 📦 Instalación de Node.js (Ubuntu)

Node.js es un entorno de ejecución que permite correr JavaScript fuera del navegador, esencial para el desarrollo backend y para utilizar herramientas modernas de frontend.

> Ejecutar los comandos en **verde**.
> Si aparece un error, reiniciar desde el principio.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install curl -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
node -v                      # Chequear que esté instalado
```

### ✅ Notas de Instalación:

*   `nvm` es un **Node Version Manager**, facilita la gestión de múltiples versiones de Node.js.
*   `--lts` instala la versión **Long Term Support**, recomendada para la mayoría de los proyectos.

---

## 🧠 Tipos de Datos y Variables

### Declaración de Variables

*   `const`: Para valores constantes que **no pueden ser reasignados**.
    ```javascript
    const PI = 3.14;
    ```
*   `let`: Para variables cuyo valor **puede cambiar**.
    ```javascript
    let contador = 10;
    contador = 11; // Válido
    ```
> 💡 **Buena práctica**: Usa `const` por defecto y cambia a `let` solo cuando necesites reasignar la variable. Evita usar `var` por su comportamiento menos predecible.

### Tipos de Datos Primitivos

| Tipo | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `number` | Números, tanto enteros como decimales. | `const edad = 25;` |
| `string` | Cadenas de texto. | `const nombre = "Juan";` |
| `boolean` | Valores de verdadero o falso. | `const esValido = true;` |
| `null` | Representa la ausencia intencional de un valor. | `let usuario = null;` |
| `undefined`| Una variable que ha sido declarada pero no asignada. | `let direccion;` |

### Tipos de Datos Estructurados

#### Objetos

Similares a los diccionarios de Python, son colecciones de pares clave-valor. En esta materia, su uso se centrará en el manejo de formato **JSON**.

```javascript
const persona = {
  nombre: "Pepito Perez",
  edad: 24,
  "ciudad de origen": "Buenos Aires"
};

// Recorrer un objeto
for (let key in persona) {
  console.log(`clave: ${key} / valor: ${persona[key]}`);
}

// Convertir objeto a string (JSON)
const personaString = JSON.stringify(persona);

// Convertir string (JSON) a objeto
const personaObjeto = JSON.parse(personaString);
```

#### Arrays (Listas)

Son un tipo especial de objeto, utilizado para almacenar listas de valores.

```javascript
const nombres = ["Juan", "Pedro", "Maria", "Ana"];

// Recorrer con for clásico
for (let i = 0; i < nombres.length; i++) {
  console.log(nombres[i]);
}

// Recorrer con for...of (preferido para listas)
for (const nombre of nombres) {
  console.log(nombre);
}

// Recorrer con forEach
nombres.forEach(function(nombre) {
  console.log(nombre);
});
```
> ⚠️ **Importante**: El bucle `for...in` se usa para objetos, mientras que `for...of` se usa para arrays y otros iterables.

---

## 🔧 Funciones

Las funciones son bloques de código reutilizables. En JavaScript, son "ciudadanos de primera clase" (`first-class citizens`), lo que significa que pueden ser tratadas como cualquier otro valor: asignadas a variables, pasadas como argumentos, etc.

### Función Clásica
```javascript
function modulo(x, y) {
  const sumaCuadrados = x*x + y*y;
  const resultado = Math.sqrt(sumaCuadrados);
  return resultado;
}
```

### Función Flecha (Arrow Function)
Una sintaxis más corta y moderna.
```javascript
// (argumentos) => { cuerpo de la función }
const modulo = (x, y) => {
  return Math.sqrt(x*x + y*y);
};

// Si solo hay una línea de código que es el return, se puede simplificar:
const suma = (x, y) => x + y;
```

### Funciones como Valores
Las funciones pueden ser pasadas como argumentos a otras funciones, lo cual es muy común en JavaScript.
```javascript
const numeros = [1, 2, 3, 4, 5, 6];

// Se pasa una función anónima al método .filter()
const filtrados = numeros.filter(x => x % 2 === 0); // resultado: [2, 4, 6]
```

---

## 🌐 Bonus Track: `fetch` y Promesas

La función `fetch` se usa para realizar peticiones de red (por ejemplo, a una API). Devuelve un objeto especial llamado `Promise` (Promesa), que representa un valor que puede estar disponible *ahora*, en el *futuro*, o *nunca*.

```javascript
const pokemonURL = "https://pokeapi.co/api/v2/pokemon?limit=3&offset=0";

fetch(pokemonURL)
  .then(response => response.json()) // Convierte la respuesta a JSON
  .then(json => console.log(json));   // Trabaja con el JSON final
```
El resultado de este código sería un objeto con la lista de los primeros 3 Pokémon.

---