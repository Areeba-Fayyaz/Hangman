import time
def count_down(n):
    print(n)
    time.sleep(0.75)
    if n==1:
        print('start!')
        return
    count_down(n-1)
    
