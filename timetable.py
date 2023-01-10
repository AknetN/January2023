# Timetable generator

print('Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time', 'Break')
subjects_list = ['History + Politics', 'Music', 'English', 'Crafts', 'Maths', 'Physics', 'IT', 'History + Politics + Science', 'Sport', 'German', 'Afterclasses activitie', 'Religion', 'Class Time', 'Break']

print('Lessons for Monday')

lesson_time = ['7:50', '8:40', '9:45', '10:35', '11:35', '12:20', '13:05', '13:50', '14:35']
only_monday = []
lesson_number = int(input('How many lessons do you have today? '))
for i in range(lesson_number):
    print(
        'Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time',
        'Break')
    subject = input('Choose any subject from the list above: ')
    only_monday.append(subject)

print('Your schedule for Monday is: ')

for i in range(len(only_monday)):
    print(only_monday[i], '(', lesson_time[i], ')')



print('Now choose lessons for Tuesday')
only_tuesday = []
lesson_number = int(input('How many lessons do you have today? '))
for i in range(lesson_number):
    print(
        'Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time',
        'Break')
    subject = input('Choose any subject from the list above: ')
    only_tuesday.append(subject)

print('Your schedule for Tuesday is: ')

for i in range(len(only_tuesday)):
    print(only_tuesday[i], '(', lesson_time[i], ')')




print('Now choose lessons for Wednesday')
only_wednesday = []
lesson_number = int(input('How many lessons do you have today? '))
for i in range(lesson_number):
    print(
        'Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time',
        'Break')
    subject = input('Choose any subject from the list above: ')
    only_wednesday.append(subject)

print('Your schedule for Wednesday is: ')

for i in range(len(only_wednesday)):
    print(only_wednesday[i], '(', lesson_time[i], ')')




print('Now choose lessons for Thursday')
only_thursday = []
lesson_number = int(input('How many lessons do you have today? '))
for i in range(lesson_number):
    print(
        'Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time',
        'Break')
    subject = input('Choose any subject from the list above: ')
    only_thursday.append(subject)

print('Your schedule for Thursday is: ')

for i in range(len(only_thursday)):
    print(only_thursday[i], '(', lesson_time[i], ')')




print('Now choose lessons for Friday')
only_friday = []
lesson_number = int(input('How many lessons do you have today? '))
for i in range(lesson_number):
    print(
        'Choose subjects from the list: History + Politics, Music, English, Crafts, Maths, Physics, IT, History + Politics + Science, Sport, German, Afterclasses activitie, Religion, Class Time',
        'Break')
    subject = input('Choose any subject from the list above: ')
    only_friday.append(subject)

print('Your schedule for Friday is: ')

for i in range(len(only_friday)):
    print(only_friday[i], '(', lesson_time[i], ')')



print('Your timetable for the whole week is: ')
print('Monday: ')
for i in range(len(only_monday)):
    print(only_monday[i], '(', lesson_time[i], ')')
print('Tuesday: ')
for i in range(len(only_tuesday)):
    print(only_tuesday[i], '(', lesson_time[i], ')')
print('Wednesday: ')
for i in range(len(only_wednesday)):
    print(only_wednesday[i], '(', lesson_time[i], ')')
print('Thursday: ')
for i in range(len(only_thursday)):
    print(only_thursday[i], '(', lesson_time[i], ')')
print('Friday: ')
for i in range(len(only_friday)):
    print(only_friday[i], '(', lesson_time[i], ')')


print('Have a wonderful weekend!!!! :)')



