def insertion_sort(A):
    for i in range(1, len(A)):
        item = A[i]
        j = i-1
        while j >= 0 and A[j] > item:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = item

a = []

with open('input.txt', 'r') as input:
    line = input.read().split()
    for i in range(len(line)):
        a.append(int(line[i]))

insertion_sort(a)

with open('output.txt', 'w+') as output:
    output.write(str(a))
