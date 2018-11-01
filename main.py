#!/usr/bin/env python3
"""
Entry module of the app
"""

import argparse
import importlib
import inspect
from colorama import init, Fore, Style

__author__ = 'Giancarlo Soverini'
__version__ = '0.1.0'
__license__ = 'MIT'

# Init colorama
init(autoreset=True)


def main():
    """ Main entry point of the app """

    # Initialize argument parser
    parser = argparse.ArgumentParser(description='Run scripts containing exercises.')

    parser.add_argument('module_n', type=int,
                    help='the number of the module containing the exercises')

    parser.add_argument('exercise', type=str, nargs='?',
                help='the name of the exercise inside a module')

    # Parse arguments from CLI
    args = parser.parse_args()

    try:
        # Lazily import the module whose number is passed from the CLI
        lazy_module = importlib.import_module(f'exercises.module_{args.module_n}')

    # Handle the exception in case the module is not found in the /exercises folder
    except ModuleNotFoundError as error:
        print('\n')
        print(Style.BRIGHT + f'    Sorry, could\'nt find module_{args.module_n} 🙄')
        print('    Remember that modules should be named like this: ' + Style.BRIGHT + 'module_<integer>')
        print('\n')
        print(Fore.RED + f'    {error.msg}')
        print('\n')
        exit(1)

    # Get the list of functions inside the imported module
    list_of_functions = inspect.getmembers(lazy_module, inspect.isfunction)

    # If no name of any function is passed through CLI,
    # print out the list of available functions in the module and exit the process
    if (args.exercise == None):
        print_list_of_functions(f'exercises.module_{args.module_n}', list_of_functions)
        exit(0)

    try:
        # Search a function whose name is identical to the exercise arg
        # passed throug CLI
        exercise = next(fn for fn in list_of_functions if fn[0] == args.exercise)

     # Handle the exception in case iteratition through the list of functions
     # didn't find any match
    except StopIteration as error:
        print('\n')
        print(Fore.RED + Style.BRIGHT
            + f'    Sorry, could\'nt find any function called {args.exercise} inside module_{args.module_n} 😕')
        print_list_of_functions(f'exercises.module_{args.module_n}', list_of_functions)
        exit(1)


    # Execute the function if a match has been found in the list of available functions
    exercise[1]()


def print_list_of_functions(module_name, fn_list):
    """Print on console a list of functions and their docs"""

    print('\n')
    print(f'    List of available functions inside {module_name}:')

    for fn in fn_list:
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f'    - {fn[0]}')
        print(Fore.LIGHTBLUE_EX + f'        {fn[1].__doc__}')
    print('\n')


if __name__ == '__main__':
    """ This is executed when run from the command line """
    main()
