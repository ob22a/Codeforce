t = int(input())
for _ in range(t):
    x = int(input())
    
    # Guaranteed solution approach is to generate x+1 primes and then use them to generate sol
    # We won't face collision and set is not needed 

    def generate_primes(size):
        primes = [2]
        num = 3

        while len(primes)!=size:
            isPrime = True

            for prime in primes:
                if prime*prime>num:
                    break

                if num%prime == 0:
                    isPrime=False
                    break
            
            if isPrime:
                primes.append(num)
            num+=1
        
        return primes
    
    primes = generate_primes(x+1)
    #print(primes)
    sol = [primes[i]*primes[i+1] for i in range(x)]

    print(*sol)