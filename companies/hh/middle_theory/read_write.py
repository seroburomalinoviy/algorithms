with open('input.txt', 'r') as input:
    data = input.read()

print(type(data))
print(data)
print(r''.format(data))
print(data.split())

with open('output.txt', 'w') as output:
    for line in data:  # отдает файл по строкам
        output.write(data)