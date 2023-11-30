# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print("*", end="")
#     print("")

a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)

a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)
