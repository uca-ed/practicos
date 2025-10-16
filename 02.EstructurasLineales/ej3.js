// Representar listas por medio de celdas con enlace simple.

class Nodo {
    constructor(valor) {
        this.valor = valor;
        this.siguiente = null;
    }
}

class ListaSimple {
    constructor() {
        this.cabeza = null; // primer nodo
        this._size = 0;
    }

    // Inserta al principio
    addFirst(valor) {
        const nodo = new Nodo(valor);
        nodo.siguiente = this.cabeza;
        this.cabeza = nodo;
        this._size++;
        return nodo;
    }

    // Inserta al final
    addLast(valor) {
        const nodo = new Nodo(valor);
        if (!this.cabeza) {
            this.cabeza = nodo;
        } else {
            let cur = this.cabeza;
            while (cur.siguiente) cur = cur.siguiente;
            cur.siguiente = nodo;
        }
        this._size++;
        return nodo;
    }

    // Elimina el primer elemento y lo devuelve (o undefined si vacía)
    removeFirst() {
        if (!this.cabeza) return undefined;
        const val = this.cabeza.valor;
        this.cabeza = this.cabeza.siguiente;
        this._size--;
        return val;
    }

    // Elimina la primera ocurrencia del valor y devuelve true si se eliminó
    remove(valor) {
        if (!this.cabeza) return false;
        if (this.cabeza.valor === valor) {
            this.cabeza = this.cabeza.siguiente;
            this._size--;
            return true;
        }
        let prev = this.cabeza;
        let cur = this.cabeza.siguiente;
        while (cur) {
            if (cur.valor === valor) {
                prev.siguiente = cur.siguiente;
                this._size--;
                return true;
            }
            prev = cur;
            cur = cur.siguiente;
        }
        return false;
    }

    // Busca la primera ocurrencia y devuelve el nodo o null
    find(valor) {
        let cur = this.cabeza;
        while (cur) {
            if (cur.valor === valor) return cur;
            cur = cur.siguiente;
        }
        return null;
    }

    size() {
        return this._size;
    }

    isEmpty() {
        return this._size === 0;
    }

}

