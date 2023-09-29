#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    num_args = len(argv)
    
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print(f'Number of argument{"(s)" if num_args != 1 else ""}: {num_args}{"." if num_args > 1 else ""}')
        print("Arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f'{i}: {arg}')

if __name__ == "__main__":
    main()
