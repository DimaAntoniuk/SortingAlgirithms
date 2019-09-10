def selection_sort(A):
    for i in range(len(A)):
        lowest_el_index = i
        for j in range(i+1, len(A)):
            if A[j]<a[lowest_el_index]:
                lowest_el_index = j
        A[i], A[lowest_el_index] = A[lowest_el_index], A[i]

a = []

with open('input.txt', 'r') as input:
    line = input.read().split()
    for i in range(len(line)):
        a.append(int(line[i]))

selection_sort(a)

with open('output.txt', 'w+') as output:
    output.write(str(a))
