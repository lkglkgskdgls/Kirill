# k, l =[], []
# for i in range(1,11):
#     k.append(10 -1)
# for i in range(1,11):
#     l.append(k[5] - k[i-1])
# print(k)
# print(l)
#
#
# k,l = list(range(1,11)), list(range(1,11))
#
# for i in range(1,11):
#     k[i-1] = 10-i
# for i in range(1,11):
#     l[i-1]=k[5]-k[i-1]
# print(k)
# print(l)
# print({len([value for value in l if value < 0])})


k,l = list(range(1, 11)), list(range(1, 11))

for i in range(1, 11):
    k[i-1] = 10-i
for i in range(1, 11):
    l[i-1] = k[5]-k[i-1]
print(k)
print(l)
count_k = 0
for valve in k:
    if valve < 0:
        count_k += 1
count_l = 0
for valve in l:
    if valve < 0:
        count_l += 1
print({count_k + count_l})

