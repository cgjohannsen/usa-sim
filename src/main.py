import argparse
import csv

from task import *
from edf_alg import *

def read_csv(filename):
    task_set = []

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            task_set.append(Task(row[0], row[1], row[2], row[3]))

    return task_set

def main():
    # PArse command line input
    parser = argparse.ArgumentParser(description='Simulate uniprocessor algorithms.')
    parser.add_argument('file', help='csv file input with task set')

    # Parse csv
    args = parser.parse_args()
    task_set = read_csv(args.file)

    # EDF schedule
    edf_sched = edf_schedule(task_set)
    if edf_sched is None:
        print("Not schedulable")
    else:
        for t in edf_sched:
            print(t.task.id)

if __name__ == "__main__":
    main()
