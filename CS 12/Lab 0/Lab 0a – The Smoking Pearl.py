def pearl_smoke_count(n: int, k: int):
    ans: int = n
    prev_n: int = n
    
    while True:
        n //= k
        ans += n
        n += prev_n % k
        
        if prev_n == n:
            break
        
        prev_n = n
        
    return ans


assert pearl_smoke_count(10, 2) == 19
assert pearl_smoke_count(4, 3) == 5
assert pearl_smoke_count(10, 3) == 14