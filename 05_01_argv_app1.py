print('Task 1. app1.py')
# The application in this file will read the command line options using sys.argv.
#
# If one of the options is --help, it should output a small help text.
#
# If one of the options is --fast is should print the text "fast mode enabled" to the command line.
#
# If --fast is not one of the options it should print the text "slow mode enabled" to the command line.



import sys

file_name = sys.argv[0]
other_data = sys.argv[1:]

if '-h' in other_data or '--help' in other_data:
    print('This is a help message')
elif '-f' in other_data or '--fast' in other_data:
    print('Fast mode enabled')
else:
    print('Slow mode enabled')