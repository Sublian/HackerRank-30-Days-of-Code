# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d={}
for i in range(n):
    name, number = input().split(' ')
    d[name]=number
    
while True:
    try:
        query = input().strip()
        if query in d:
            print(query + "=" + d[query])
        else:
            print("Not found")
    except EOFError:
        break
