class Task:
    def __init__(self, ID, P, C, D):
        self.id = ID
        self.p = P
        self.c = C
        self.d = D

class Sched_Task:
    def __init__(self, Task, S, E):
        self.task = Task
        self.start_time = S
        self.end_time = E
