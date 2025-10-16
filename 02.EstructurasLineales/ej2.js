// pila.js
// Uso: node pila.js pilas.txt

const fs = require("fs");

// ----- Pila sobre arreglo (capacidad fija) -----
class Pila {
  constructor(capacidad = 10) {
    this.arr = new Array(capacidad);
    this.cap = capacidad;
    this.tope = -1; // pila vacía => -1
  }

  apilar(valor) { // PUSH
    if (this.tope + 1 === this.cap) {
      console.warn("Pila llena. No se puede apilar:", valor);
      return false;
    }
    this.arr[++this.tope] = valor;
    return true;
  }

  desapilar() { // POP
    if (this.tope < 0) {
      console.warn("Pila vacía. No se puede desapilar.");
      return undefined;
    }
    const v = this.arr[this.tope];
    this.arr[this.tope] = undefined; // opcional
    this.tope--;
    return v;
  }

  size() { return this.tope + 1; }

  toArrayTopDown() {
    const out = [];
    for (let i = this.tope; i >= 0; i--) out.push(this.arr[i]);
    return out;
  }
}

// ----- Helpers (igual que en colas) -----
function parseValue(raw) {
  const s = raw.trim();
  if (!s) return "";
  const m = s.match(/^"(.*)"$/) || s.match(/^'(.*)'$/);
  if (m) return m[1];
  const n = Number(s);
  return Number.isFinite(n) && /^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?$/.test(s) ? n : s;
}

// ----- Main (igual estilo que en colas) -----
const file = process.argv[2];
if (!file) {
  console.error("Uso: node pila.js pilas.txt");
  process.exit(1);
}

let text;
try {
  text = fs.readFileSync(file, "utf8");
} catch (e) {
  console.error("No pude leer el archivo:", e.message);
  process.exit(1);
}

const pila = new Pila(10); // misma capacidad por defecto que colas
const lines = text.split(/\r?\n/);

for (let i = 0; i < lines.length; i++) {
  let line = lines[i].replace(/\/\/.*$/, "").trim();
  if (!line) continue;

  const firstSpace = line.indexOf(" ");
  const op = (firstSpace === -1 ? line : line.slice(0, firstSpace)).toUpperCase();
  const payload = firstSpace === -1 ? "" : line.slice(firstSpace + 1).trim();

  if (op === "PUSH" || op === "APILAR") {
    if (!payload) {
      console.warn(`Línea ${i + 1}: falta el valor a apilar.`);
      continue;
    }
    pila.apilar(parseValue(payload));
  } else if (op === "POP" || op === "DESAPILAR") {
    pila.desapilar();
  } else {
    console.warn(`Línea ${i + 1}: operación desconocida "${op}".`);
  }
}

// ----- Resultado final (mismo formato que colas) -----
console.log("\n--- RESULTADO FINAL ---");
console.log("Tamaño:", pila.size());
console.log("Índice tope:", pila.tope);
console.log("[top → base]:", pila.toArrayTopDown());
