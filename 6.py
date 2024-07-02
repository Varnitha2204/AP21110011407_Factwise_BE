n = int(input())
for i in range(n):
    s = input()
    s1 = s.split("-")
    s2 = "".join(s1)
    s3 = s2.split(" ")
    print(len("".join(s3)))
