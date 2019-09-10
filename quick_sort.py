def partition(A, low, high):
    pivot = A[(high + low) // 2]
    i = low - 1
    j = high + 1
    while True:

        i += 1
        if A[i] < pivot:
            i += 1

        j -= 1
        if A[j] > pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]

def quick_sort(A):
    def _quick_sort(B, low, high):
        if low < high:
            split_item = partition(B, low, high)
            _quick_sort(B, low, split_item)
            _quick_sort(B, split_item + 1, high)
    _quick_sort(A, 0, len(A) - 1)

a = []

with open('input.txt', 'r') as input:
    line = input.read().split()
    for i in range(len(line)):
        a.append(int(line[i]))

quick_sort(a)

with open('output.txt', 'w+') as output:
    output.write(str(a))
