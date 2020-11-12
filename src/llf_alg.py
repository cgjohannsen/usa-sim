import sys
from task import *

class LLF:

	def schedule(self, task_set):
		# task_set = [Task0, Task1, ... , Taskn]
		if not self.sched_test(task_set):
			return None

		# Find LCM of Periods
		periods = []
		for t in task_set:
			periods.append(t.p)
		hyperperiod = find_lcm(periods)

		# Create a computation time remaining array
		comp_remaining = [t.c for t in task_set]

		# Create a deadlines array
		deadlines = [t.d for t in task_set]

		# Create a laxities array
		laxities = [t.d for t in task_set]

		cur_task = -1 # task scheduled for current time step
		prev_task = -1 # task scheduled for previous time step
		prev_task_start = 0
		schedule = []
		for time in range(hyperperiod):
			# Calculate next deadlines
			for i, t in enumerate(task_set):
				deadlines[i] = (int(time / t.p) * t.p) + t.d
				if time > 0 and time % t.p == 0:
					comp_remaining[i] = t.c
				laxities[i] = deadlines[i] - (time + comp_remaining[i])

			# Find task with earliest deadline
			# If no task with remaining computation time is before its current
			# deadline, go inactive
			least_laxity = hyperperiod + 1
			for i in range(len(task_set)):
				if deadlines[i] >= time and laxities[i] < least_laxity and comp_remaining[i] > 0:
					least_laxity = laxities[i]
					cur_task = i

			# If different task is scheduled or current task is completed,
			# add previous task to schedule
			if cur_task is not prev_task and not time == 0:
				schedule.append(Sched_Task(task_set[prev_task], prev_task_start, time))
				prev_task_start = time

			comp_remaining[cur_task] -= 1
			prev_task = cur_task
			cur_task = -1

		return schedule

	def sched_test(self, task_set):
		# If -- schedulability test success, return True
		sum = 0
		for task in task_set:
			sum += (int(task.c) / int(task.p))
		if sum <= 1:
			return True
		# Else -- return False
		return False
