import sys

from task import *

class EDF:

	def schedule(task_set):
		# task_set = [Task0, Task1, ... , Taskn]
		# Create the schedule
		time = 0
		i = 0
		schedule = []
		while time < lcm_period(task_set):
			earliest_deadline = sys.maxsize
			cur_task = None
			cur_task_start = 0

			for t in task_set:
				if int(t.d) < earliest_deadline:
					earliest_deadline = int(t.d)
					sched_task = t

			if i > 0 and sched_task is not schedule[i-1]:
				if not schedule:
					schedule.append(Sched_Task(cur_task, 0, time))
				else:
					schedule.append(Sched_Task(cur_task, cur_task_start, time))
				i += 1
				cur_task_start = time

			time += 1

		return schedule

	def sched_test(task_set):
		schedulable = False

		# If -- schedulability test success, return True
		sum = 0
		for task in task_set:
			sum = sum + (int(task.c) / int(task.p))

		if sum <= 1:
			schedulable = True

		# Else -- return False
		return schedulable
