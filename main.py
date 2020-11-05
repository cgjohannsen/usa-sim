import argparse
import csv

from task import *

def read_csv(filename):
    task_set = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data = str(row).split(',')
            task_set.append(Task(data[0], data[1], data[2], data[3]))

    return task_set 

def main():
    parser = argparse.ArgumentParser(description='Simulate uniprocessor algorithms.')
    parser.add_argument('file', help='csv file input with task set')

    args = parser.parse_args()
    task_set = read_csv(args.file)

    for task in task_set:
        print(task.id)

if __name__ == "__main__":
    main()
