import sys

from task import Task, Sched_Task

def edf_schedule(task_set):
	# task_set = [Task0, Task1, ... , Taskn]
	if not edf_sched_test(task_set):
		return None

	# Create the schedule
	time = 0
	done = False
	schedule = []
	while not done:
		earliest_deadline = sys.maxsize
		cur_task = None
		cur_task_start = 0

		for t in task_set:
			if int(t.d) < earliest_deadline:
				earliest_deadline = int(t.d)
				sched_task = t

		if time > 0 and sched_task is not schedule[time-1]:
			if not schedule:
				schedule.append(Sched_Task(cur_task, 0, time))
			else:
				schedule.append(Sched_Task(cur_task, cur_task_start, time))
			cur_task_start = time

		time = time + 1

	return schedule

def edf_sched_test(task_set):
	schedulable = False

	# If -- schedulability test success, return True
	sum = 0
	for task in task_set:
		sum = sum + (int(task.c) / int(task.p))

	if sum <= 1:
		schedulable = True

	# Else -- return False
	return schedulable
