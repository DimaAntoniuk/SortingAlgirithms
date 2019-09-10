def bubble_sort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(A)):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swapped = True
a = []
with open('input.txt', 'r') as input:
    string = input.read().split()
    for i in range(len(string)):
        a.append(int(string[i]))
bubble_sort(a)
with open('output.txt', 'w+') as output:
    output.write(str(a))
