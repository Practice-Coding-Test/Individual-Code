#10773 제로
stack= list()
n= int(input()) 
for i in range (n):
    num = int(input()) 
    if num != 0:
        stack.append(num) 
    else:
        stack.pop() 

print(sum(stack))