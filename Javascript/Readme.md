# Javascript

En orden van Javascript > Ecmascript > Typescript

---

## 📦 Instalación de Node.js (Ubuntu)

> Ejecutar los comandos en **verde**.
> Si aparece un error, reiniciar desde el principio.

```bash
sudo apt update
sudo apt upgrade -y          # Ojo: tarda mucho
sudo apt install curl -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm alias default 22.14.0
node -v                      # Chequear que esté instalado
```

### ✅ Notas:

* `nvm` es un **Node Version Manager**, facilita la gestión de múltiples versiones de Node.js.
* `--lts` instala la versión **Long Term Support**, recomendada para producción.
* `nvm alias default` configura la versión por defecto.

---

## 🧮 Variables y Constantes en JavaScript

### `const` (constante)

```js
const PI = 3.14159265359;
```

* No puede ser reasignada.
* Intentar hacer `PI = 3;` lanza un error:

```js
TypeError: Assignment to constant variable.
```

### `let` (variable)

```js
let alumnosCursando = 237;
alumnosCursando = 122; // ✅ Reasignación permitida
```

### ✅ Notas:

* Usar `const` siempre que el valor **no vaya a cambiar**.
* Usar `let` cuando **esperás modificar el valor**.
* Evitá `var`, es obsoleto por su comportamiento de hoisting.

---

## 🧠 Tipos de Datos en JavaScript

```js
const alumnos = 237              // number
const precio = 1392.50           // number
const nombre = "Bruno"           // string
const esDomingo = false          // boolean

const persona = { nombre: "pepe", edad: 26 } // object
const numeros = [1, 2, 3]        // object (array)
let valorInicial = null          // object

const ultimoDigitoDePI = undefined // undefined
```

### ✅ Notas:

#### 🎯 Tipos primitivos:

* `number`: Números enteros y decimales.
* `string`: Cadenas de texto entre comillas (`"texto"` o `'texto'`).
* `boolean`: `true` o `false`.
* `undefined`: Variable declarada pero **sin valor asignado**.
* `null`: Valor intencionalmente vacío o "sin valor". Aunque el tipo es `object`, es un valor primitivo. **valor asignado**

#### 🧱 Tipos estructurados:

* `object`: Agrupación de pares clave/valor. Incluye arrays, funciones y objetos literales.
* `array`: Es un tipo especial de `object`. En JS no existe un tipo separado para arrays.

> 💡 Tip: Podés usar `typeof` para verificar el tipo:

```js
typeof nombre         // "string"
typeof numeros        // "object"
typeof null           // "object" (quirk histórico)
typeof undefined      // "undefined"
```

---

