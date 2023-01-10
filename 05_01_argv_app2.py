print('Task 2. app1.py')
# The application in this file will read the command line options using getopt().
#
# This application should accept the flags -h or --help to print a help text.
#
# This application should let the user set a name with the option -n [NAME] or --name=[NAME].
#
# If a name is given, the application should output Good Morning [NAME]!. If no name is specified, it should just output Good Morning folks!

import sys
import getopt

file_name = sys.argv[0]
other_data = sys.argv[1:]

rec_data, not_rec_data = getopt.getopt(other_data, 'h:n', ['help=', 'message=', 'name='])
name = None

for item in rec_data:
    if item[0] == '-h' or item[0] == '--help':
        print('Some help message')
    elif item[0] == '--name' or item[0] == '-n' or item[0] == 'name':
        print('Good Morning, ', item[1])
        name = item[1]
if not name:
        print('Good Morning, folks!')
