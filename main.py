import argparse

def main():
    parser = argparse.ArgumentParser(description='Simulate uniprocessor algorithms.')
    parser.add_argument('file', help='csv file input with task set')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
