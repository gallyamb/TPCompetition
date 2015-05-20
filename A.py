def primes():
    yield 2; yield 3; yield 5; yield 7;
    bps = (p for p in primes())             
    p = next(bps) and next(bps)
    q = p * p
    sieve = {} 
    n = 9          
    while True:
        if n not in sieve:  
            if n < q:                 
                yield n            
            else:
                p2 = p + p               
                sieve[q + p2] = p2    
                p = next(bps); q = p * p    
        else:
            s = sieve.pop(n); nxt = n + s   
            while nxt in sieve: nxt += s    
            sieve[nxt] = s              
        n += 2                           
 
import itertools
def primes_up_to(limit):
    yield from itertools.takewhile(lambda p: p <= limit, primes())


num = int(input())

nums = []


def get_devider(num):
    for i in primes_up_to(num):
        if num % i == 0:
            return i
    return 1


nums.append(get_devider(num))
num = int(num / nums[-1])

nums.append(get_devider(num))
nums.append(int(num / nums[-1]))
print(' '.join(map(str, nums)))
