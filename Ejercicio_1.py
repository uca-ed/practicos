# EJERCICIO 1

class queue():
    def __init__(self):
        self.queue = [None]*5
        self.len_q = 5
        self.top = 0
        self.bot = 0
        self.count = 0
    
    def enqueue(self,value):
        if self.count >= self.len_q:
            return "the queue is full"
        if self.top == self.len_q:
            self.top = self.top%self.len_q
        
        self.queue[self.top] = value
        self.top += 1
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return "the queue is empty"
        if self.bot == self.len_q:
            self.bot = self.bot%self.len_q

        self.queue[self.bot] = None
        self.bot += 1
        self.count -= 1

def main():
    mi_lista = queue()
    mi_lista.enqueue(5)
    mi_lista.enqueue(25)
    mi_lista.enqueue(3)
    mi_lista.enqueue(2)
    mi_lista.enqueue(1)
    mi_lista.dequeue()

    print(mi_lista.queue)

main()
        
