# name = input("Name: ")
#
# out_file = open('name.txt', 'w')
# print(name , file = out_file)
# out_file.write(name)
# out_file.close
#
#
# out_file = open('name.txt', 'r')
# name = out_file.read()
# print(f"Your name is {name}")
# out_file.close

with open('numbers.txt', 'r') as out_file:
    content = out_file.read()
    print(content)

out_file = open('numbers.txt', 'r')
total_number = 0
for line in range(2):
    number = float(out_file.readline())
    total_number += number
print(total_number)
out_file.close

out_file = open('numbers.txt', 'r')
total_number = 0
for line in out_file.readlines():
   number = float(line.strip())
   total_number += number
print(total_number)
