import time
N = 300000


a = [1] * N
start = time.time()
for i in range(N):
    del a[0]
end = time.time()
print("Del Elapsed time: %d" % (end - start))


a = [1] * N
start = time.time()
for i in range(N):
    del a[len(a) // 2 - 1]
end = time.time()
print("Del mid Elapsed time: %d" % (end - start))


b = [1] * N
start = time.time()
for i in range(N):
    b.pop()
end = time.time()
print("Pop Elapsed time: %d" % (end - start))


c = [1] * N
start = time.time()
for i in range(N):
    del c[-1]
end = time.time()
print("Del last Elapsed time: %d" % (end - start))



d = {k:k for k in range(N)}
start = time.time()
for i in range(N):
    del d[i]
end = time.time()
print("Del dict Elapsed time: %d" % (end - start))



a = []
start = time.time()

for i in range(10**8):
    a.append(1)
end = time.time()
print("Elapsed time: %d" % (end - start))

'''
10^7 - 7 sec
10^8 - 85 sec
10^12 - 10000000 sec
'''