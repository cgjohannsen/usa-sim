# RMS - Rate Monotomic Scheduling
# Task with smallest period is given highest priority
# At any time, the highest priority task is executed


import math
from src.task import Task, Sched_Task
from math import gcd


def find_lcm(nums):
	lcm = nums[0]
	for i in nums[1:]:
		lcm = lcm*i//gcd(lcm, i)
	return lcm


class RMS:
	
	def schedule(self, task_set):
		# Order the task_set (smallest period --> largest period)
		sorted_task_set = sorted(task_set, key=lambda x: x.p, reverse=False)

		# task_set = [Task0, Task1, ... , Taskn]
		if not self.sched_test(sorted_task_set):
			return None

		num_tasks = len(task_set)
		
		# Find LCM of Periods
		periods = []
		for t in task_set:
			periods.append(t.p)
		time_schedule_repeats = find_lcm(periods)

		# Create a "ready" array that maps to the sorted_task_set
		ready_arr = [True for i in range(num_tasks)]

		# Create a computation time remaining array
		comp_remaining = [t.c for t in sorted_task_set]

		# Create the schedule
		schedule = []
		running_task_i = -1
		task_started_time = 0
		for time_step in range(time_schedule_repeats):

			# subtract from the comp time remaining
			# if comp time remaining == 0, running_task_i = -1, ready_i = False
			if running_task_i > -1:
				comp_remaining[running_task_i] -= 1
				# Task has finished
				if comp_remaining[running_task_i] == 0:
					schedule.append(Sched_Task(sorted_task_set[running_task_i], task_started_time, time_step))
					ready_arr[running_task_i] = False
					running_task_i = -1

			for i, t in enumerate(sorted_task_set):
				# The task arrives
				# if not ready_arr[i] and (time_step % t.p == 0):
				# 	ready_arr[i] = True
				# 	comp_remaining[i] = t.c

				if time_step % t.p == 0:
					if not ready_arr[i]:
						ready_arr[i] = True
						comp_remaining[i] = t.c
					else:
						if time_step > 0:
							return None

				# The task is ready to run, does it need to preempt?
				if ready_arr[i]:
					# If nothing is running, this task is now set to run
					if running_task_i == -1:
						running_task_i = i
						task_started_time = time_step

					# This task must preempt the currently running task
					elif t.p < sorted_task_set[running_task_i].p:
						schedule.append(Sched_Task(sorted_task_set[running_task_i], task_started_time, time_step))
						running_task_i = i
						task_started_time = time_step

					# Nothing else to do
					else:
						continue

		return schedule

	def sched_test(self, task_set):
		num_tasks = len(task_set)
		res = 0
		for i, t in enumerate(task_set):
			res += t.c + t.p
		if res <= num_tasks * (math.pow(2, 1 / num_tasks) - 1):
			return True
		if self.exact_analysis(task_set):
			return True
		return False
	
	def exact_analysis(self, task_set):
		# Do exact analysis. If successful, return true. Else, false
		for i, t in enumerate(task_set):
			if not self.do_exact_analysis(task_set[0:i+1], i):
				return False
		return True

	def do_exact_analysis(self, sub_task_set, analyzing_task_i):
		print("Doing Exact Analysis with task:  ", end='')
		print(sub_task_set[analyzing_task_i].id)
		print("Num tasks: " + str(len(sub_task_set)))
		cur_total = 0
		i = 0
		print("t"+str(i)+" = ", end='')
		for t in sub_task_set:
			cur_total += t.c
			print(t.c, end=" + ")
		print("0 = " + str(cur_total))
		last_total = cur_total
		cur_total = 0
		while True:
			i += 1
			print("t" + str(i) + " = ", end='')
			for t in sub_task_set:
				multiplier = math.ceil(last_total/t.p)
				cur_total += multiplier * t.c
				print(str(multiplier) + "*" + str(t.c), end=" + ")
			print("0 = " + str(cur_total))
			if cur_total == last_total:
				return True
			elif cur_total > sub_task_set[analyzing_task_i].p:
				return False
			else:
				last_total = cur_total
				cur_total = 0


def main():
	# t1 = Task("T1", 10, 3, 10)
	# t2 = Task("T2", 15, 4, 15)
	# t3 = Task("T3", 5, 1, 5)

	t1 = Task("T1", 10, 2, 10)
	t2 = Task("T2", 2, 1, 2)
	t3 = Task("T3", 20, 5, 20)

	ts = [t1, t2, t3]

	rms = RMS()
	s = rms.schedule(ts)
	for t in s:
		print(t.task.id + '\t' + str(t.start_time) + '\t' + str(t.end_time))


if __name__ == "__main__":
	main()
