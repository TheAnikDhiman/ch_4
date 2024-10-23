l=[]
n=int(input("Enter Lenght of List: "))
for i in range(1, n+1):
    a = int(input(f"Enter Number{i}: "))
    l.append(a)
print(sum(l))