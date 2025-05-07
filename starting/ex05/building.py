import sys

def syntax_build(args):
    """
    Syntax for building the project:
    check the syntax of the arguments and split them into
    upper-case characters, lower-case
    characters, punctuation characters, digits and spaces.
    """
    upper_case = []
    lower_case = []
    punctuation = []
    digits = []
    spaces = []

    for char in args:
        if char.isupper():
            upper_case.append(char)
        elif char.islower():
            lower_case.append(char)
        elif char in '.,;:!?-()[]{}"\'/\\|<>@#$%^&*`~':
            punctuation.append(char)
        elif char.isdigit():
            digits.append(char)
        elif char.isspace():
            spaces.append(char)
    print("Total characters:", len(args))
    print("Upper-case characters:", len(upper_case))
    print("Lower-case characters:", len(lower_case))
    print("Punctuation characters:", len(punctuation))
    print("Spaces:", len(spaces))
    print("Digits:", len(digits))
    
    

def main(args):
    if len(args) == 0:
        print("No arguments provided.")
        return
    elif len(args) > 1:
        print("Too many arguments provided.")
        return
    syntax_build(args[0])
    return 


if __name__ == "__main__":
    main(sys.argv[1:])