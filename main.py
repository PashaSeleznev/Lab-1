import csv

rows = []
with open('books.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    k1 = 0
    k2 = 0

    for row in file_reader:
        rows.append(row)
        k1 += 1
        if len(row[1]) > 30:
            k2 += 1
    print(k1 - 1)
    print(k2)
print()
print('Введите имя автора:')
search = input()

for row in rows:
    if (row[3] == search) and (float(row[7][:-3]) >= 150):
        if '#' in row[1]:
            print(row[1].replace('#', ''), row[7])
        else:
            print(row[1], row[7])

print()

k = 1
for row in rows:
    if k < 22:
        print(f'{row[3]}. {row[1]} - {row[6]}')
    k += 1
print()

rows_1 = []
for row in rows:
    row_1 = row[12].split('#')
    for i in row_1:
        if i not in rows_1:
            if i[0] == ' ':
                i = i.replace(' ', '', 1)
            rows_1.append(i)
            print(i)


print()

a = sorted(rows[1:], key=lambda x: int(x[8]), reverse=True)
print(*a[:20], sep='\n')
