import time

def merge(A, B):
    out = []
    a = b = 0
    global comp
    while a < len(A) and b < len(B):
        comp += 1
        if A[a] < B[b]:
            out.append(A[a])
            a += 1
        else:
            out.append(B[b])
            b += 1
    out += A[a:] + B[b:]
    comp += len(A)-a + len(B)-b
    return out

def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A) // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))

a = []
comp = 0
with open('input.txt', 'r') as input:
    line = input.read().split()
    for i in range(len(line)):
        a.append(int(line[i]))
start = time.time()
a = merge_sort(a)
finish = time.time()
with open('output.txt', 'w+') as output:
    output.write(str(a))
    output.write('\n')
    output.write(str(comp))
