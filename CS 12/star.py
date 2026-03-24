def who_gets_the_star(m: int, w: int, p: int, s: int):
    MAX = max(m, w, p)
    MIN = min(m, w, p)
    ppl: list[int] = [m, w,p]
    
    if s > MAX:
        return MAX
    
    if s < MIN:
        return MIN
    
    inc = 1
    while not((s - inc) in ppl or (s + inc) in ppl):
        inc += 1
        
    diff = s - inc
    if diff in ppl:
        c = ppl.count(diff)
        if c > 1:
            return "NONE"
        
        i = ppl.index(diff)
        return ppl[i]
    
    if 