magicians = ['alice', 'david', 'carolina']

print("\nThe list 'magicians' contains the following strings:")

for magician in magicians:
    print("\t" + magician)

print("\nApplying capitalization...")

loop_iteration = 0

while loop_iteration < len(magicians):
    print("\t" + magicians[loop_iteration].rjust(10), end = "\t->\t")
    magicians[loop_iteration] = magicians[loop_iteration].title()
    print(magicians[loop_iteration])
    loop_iteration += 1

print("\nSorting list...")

magicians.sort()

for magician in magicians:
    print("\t" + magician)

magicians.reverse()

print("\nReversing list...")

for magician in magicians:
    print("\t" + magician)

numerical_list = list(range(0,1000))

print(numerical_list)














