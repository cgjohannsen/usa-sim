import time

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

def lcm_period(task_set):
    # LCM of periods is the hyperperiod
    # i.e. how we know our schedule is done

    # Assemble periods
    periods = []
    periods_t = []
    for task in task_set:
        periods.append(int(task.p))
        periods_t.append(int(task.p))

    # Find LCM
    equal = False
    while not equal:
        min_index = 0
        m = min(periods_t)
        for i in range(0,len(periods_t)):
            if periods_t[i] == m:
                min_index = i

        periods_t[min_index] += periods[min_index]

        # Is this the LCM?
        equal = True
        for p1 in periods_t:
            for p2 in periods_t:
                if p1 != p2:
                    equal = False
                    break
            if not equal:
                break

    return periods_t[0]
