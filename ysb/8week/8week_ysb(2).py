import sys
#sys.stdin=open("input.txt", "r")

def DFS(L):
    global cnt
    global ans
    if L == n:
        total = int(get_total(res))
        if total == f:
            for j in res:
                ans += str(j)+' '             
           
        
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)            #여기서 L은 자리를 의미하는거
                ch[i]=0

                
def get_total(num):
    p = 0
    sum = []
    while True:
        while p<(len(num)-1):
            sum.append(num[p]+num[p+1])
            p+=1
        num=sum
        sum=[]
        p=0

        if len(num)==1:
            return num[0]
            
      
      
if __name__=="__main__": 
    n,f = map(int,input().split())
    res = [0]*n
    ch = [0] * (n+1)
    ans=''
    DFS(0)
    print(ans[:2*n-1])
   
    


    
    
    
    

   


 






        


