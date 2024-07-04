import time
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
start=time.time()#curresnt timing,,(ie;when u hit this statement at thatmoment waht is the time)
print(start,'ms')
res=fib(5)
print(res)
print(time.time()-start,'seconds')