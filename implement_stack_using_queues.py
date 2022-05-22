class Queue:
    def __init__(self):
        self.queue = []
    def push(self,val):
        self.queue.append(val)
    def pop(self):
        return self.queue.pop(0)
    def top(self):
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue)== 0:
            return True
        else:
            return False
class MyStack:
    def __init__(self):
        self.q = Queue()
        self.temp = Queue()
    def push(self, x: int) -> None:
        self.temp.push(x)
        while not self.q.isEmpty():
            self.temp.push(self.q.pop())
        self.q,self.temp = self.temp,self.q
        
    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.isEmpty()
