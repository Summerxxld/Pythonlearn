import sys
global a
global result
def judge(x,y,n):
    for i in range(n,-1,-1):
        if a[i][y]=='B':
            return 0
        if a[i][y]=='X':
            break
    for i in range(n,-1,-1):
        if a[x][i]=='B':
            return 0
        if a[x][i]=='X':
            break
    return 1

def dfs(pos,curr,n):
    if pos==n*n:
        if curr>result:
            result=curr
        return
    x=pos/n
    y=pos%n
    if a[x][y]=='.' and judge(x,y,n):
        a[x][y]='B'
        dfs(pos+1,curr+1,n)
        a[x][y]='.'
    dfs(pos+1,curr,n)

def main():
    while True:
        n=int(sys.stdin.readline())
        if n==0:
            break
        global a
        global result
        a=[list(sys.stdin.readline().strip()) for i in range(n)]
        result=0
        dfs(0,0,n)
        print(result)
    return 0    

