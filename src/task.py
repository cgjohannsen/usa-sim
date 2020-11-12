from math import gcd

class Task:
    def __init__(self, ID, P, C, D):
        self.id = ID
        self.p = int(P)
        self.c = int(C)
        self.d = int(D)

class Sched_Task:
    def __init__(self, Task, S, E):
        self.task = Task
        self.start_time = int(S)
        self.end_time = int(E)

def find_lcm(nums):
	lcm = nums[0]
	for i in nums[1:]:
		lcm = lcm*i//gcd(lcm, i)
	return lcm
