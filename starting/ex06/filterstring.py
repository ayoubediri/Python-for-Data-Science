import sys
from ft_filter import ft_filter

def main(args):
    if len(args) != 2:
        print("AssertionError: the arguments are bad.")
        return
    try:
        print(ft_filter(lambda x: len(x) > int(args[1]), args[0].split()))
    except ValueError:
        print("AssertionError: the arguments are bad.")
        return
        

if __name__ == "__main__":
    main(sys.argv[1:])