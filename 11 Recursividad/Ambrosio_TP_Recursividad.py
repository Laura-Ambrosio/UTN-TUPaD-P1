def factorial_recur(x):
    if x==0:
        return 1
    else:
        return x * factorial_recur(x-1)