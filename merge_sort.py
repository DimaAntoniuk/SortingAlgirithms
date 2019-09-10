def merge(A, B):
    out = []
    a = b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            out.append(A[a])
            a += 1
        else:
            out.append(B[b])
            b += 1
    out += A[a:] + B[b:]
    return out

def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A) // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))

a = []

with open('input.txt', 'r') as input:
    line = input.read().split()
    for i in range(len(line)):
        a.append(int(line[i]))

a = merge_sort(a)

with open('output.txt', 'w+') as output:
    output.write(str(a))
