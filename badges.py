#function for printing badges

#program that reads the number of students and prints badges
def print_label():
   print('-Golden Feather-')
   print('Name: ____')
   print('School: ____')


amount = int(input('Number of students:'))
for i in range(amount):
   print_label()
print('Done! Take your badges.')