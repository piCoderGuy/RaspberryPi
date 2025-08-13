# Recursion
# Fibonacci
def fib(x):
    # returns Fibonacci to how many places called
    #1,1,2,3,5,8,13,21,etc
    if x ==1 or x ==2:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    # say 5 called = fib called 4 times + fin called 2 times
    
print (fib(3))

def efficient_fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = efficient_fib(n-1, d) + efficient_fib (n-2, d)
        d[n] = ans
        # Builds a dictionery of known answers
        return ans

d = {1:1, 2:1}
print (efficient_fib(60, d))
print (efficient_fib(5, d))

print(d)

def score_count(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 3
    else:
        return score_count(x-1) + score_count(x-2)+score_count(x-3)

print (f'There are  {score_count(20)} possible ways to score 20 points in basketball')
