// ej1.js
// Uso: node ej1.js ej1.txt

const fs = require("fs");

// ----- Cola circular sobre arreglo, con frente y final -----
class Cola {
  constructor(capacidad = 10) {
    this.arr = new Array(capacidad);
    this.cap = capacidad;
    this.frente = 0; // índice del primer elemento
    this.final = 0;  // índice libre para encolar
    this.size = 0;   // cantidad de elementos
  }

  encolar(valor) {
    if (this.size === this.cap) {
      console.warn("Cola llena. No se puede encolar:", valor);
      return false;
    }
    this.arr[this.final] = valor;
    this.final = (this.final + 1) % this.cap;
    this.size++;
    return true;
  }

  desencolar() {
    if (this.size === 0) {
      console.warn("Cola vacía.");
      return undefined;
    }
    const valor = this.arr[this.frente];
    this.arr[this.frente] = undefined; // opcional: liberar referencia
    this.frente = (this.frente + 1) % this.cap;
    this.size--;
    return valor;
  }

  toArray() {
    const out = [];
    for (let i = 0; i < this.size; i++) {
      const idx = (this.frente + i) % this.cap;
      out.push(this.arr[idx]);
    }
    return out;
  }
}

// ----- Helpers -----
function parseValue(raw) {
  const s = raw.trim();
  if (!s) return "";
  // entre comillas
  const m = s.match(/^"(.*)"$/) || s.match(/^'(.*)'$/);
  if (m) return m[1];
  // número
  const n = Number(s);
  return Number.isFinite(n) && /^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?$/.test(s) ? n : s;
}

// ----- Main -----
const file = process.argv[2];
if (!file) {
  console.error("Uso: node ej1.js ej1.txt");
  process.exit(1);
}

let text;
try {
  text = fs.readFileSync(file, "utf8");
} catch (e) {
  console.error("No pude leer el archivo:", e.message);
  process.exit(1);
}

const q = new Cola(10);
const lines = text.split(/\r?\n/);

for (let i = 0; i < lines.length; i++) {
  // quitar comentarios y espacios
  let line = lines[i].replace(/\/\/.*$/, "").trim();
  if (!line) continue;

  // separar operación y payload exacto
  const firstSpace = line.indexOf(" ");
  const op = (firstSpace === -1 ? line : line.slice(0, firstSpace)).toUpperCase();
  const payload = firstSpace === -1 ? "" : line.slice(firstSpace + 1).trim();

  if (op === "ENQUEUE" || op === "ENCOLAR") {
    if (!payload) {
      console.warn(`Línea ${i + 1}: falta el valor a encolar.`);
      continue;
    }
    q.encolar(parseValue(payload));
  } else if (op === "DEQUEUE" || op === "DESENCOLAR") {
    q.desencolar();
  } else {
    console.warn(`Línea ${i + 1}: operación desconocida "${op}".`);
  }
}

// ----- Resultado final -----
const final = q.toArray();
console.log("\n--- RESULTADO FINAL ---");
console.log("Tamaño:", q.size);
console.log("Frente:", q.frente);
console.log("Final:", q.final);
console.log("Cola (frente → fondo):", final);
