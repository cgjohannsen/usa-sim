import argparse
import csv

from task import *
from edf_alg import EDF
from rms_alg import RMS
from llf_alg import LLF

def read_csv(filename):
    task_set = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            task_set.append(Task(row[0], row[1], row[2], row[3]))
    return task_set

def write_csv(filename, sched_set):
    to_write = []
    for t in sched_set:
        to_write.append([t.task.id, t.start_time, t.end_time])
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(to_write)

def main():
    # Parse command line input
    parser = argparse.ArgumentParser(description='Simulate uniprocessor algorithms.')
    parser.add_argument('file', help='csv file input with task set')

    # Parse csv
    args = parser.parse_args()
    task_set = read_csv(args.file)

    # RMS schedule
    rms = RMS()
    rms_sched = rms.schedule(task_set)
    if rms_sched is None:
        print("RMS not schedulable")
    else:
        write_csv("rms.csv", rms_sched)

    # EDF schedule
    edf = EDF()
    edf_sched = edf.schedule(task_set)
    if edf_sched is None:
        print("EDF not schedulable")
    else:
        write_csv("edf.csv", edf_sched)

    # LLF schedule
    llf = LLF()
    llf_sched = llf.schedule(task_set)
    if llf_sched is None:
        print("EDF not schedulable")
    else:
        write_csv("llf.csv", llf_sched)

if __name__ == "__main__":
    main()
