class Task:
    def __init__(self, ID, P, C, D):
        self.id = ID
        self.p = P
        self.c = C
        self.d = D
 

class Sched_Task:
    def __init__(self, Task, s, e):
        self.task = Task
        self.start_time = s
        self.end_time = e


