def hh(curr: int, n: int, dp: list[int]) -> int:
    if curr > n:
        return dp[-1]

    dp[curr] = 72 * dp[curr - 1] - 1296 * dp[curr - 2] - 3 * dp[curr - 4] + 108 * dp[curr - 5] - 2 * dp[curr - 8]

    return hh(curr + 1, n, dp)

def cs12_string_count(n: int) -> int:
    dp: list[int] = [0] * (n + 1)

    if n == 0:
        dp = [0]
    elif n == 1:
        dp = [0, 0]
    elif n == 2:
        dp = [0,0,0]
    elif n == 3:
        dp = [0,0,0,0]
    elif n == 4:
        dp = [0,0,0,0,1]
    elif n == 5:
        dp = [0,0,0,0,1,72]
    elif n == 6:
        dp = [0,0,0,0,1,72,3888]
    elif n == 7:
        dp = [0,0,0,0,1,72,3888,186624]
    else:
        dp[0] = 0
        dp[1] = 0
        dp[2] = 0
        dp[3] = 0
        dp[4] = 1
        dp[5] = 72
        dp[6] = 3888
        dp[7] = 186624

    ans: int = 0

    if n < 8:
        return dp[n]
    else: 
        ans = hh(8, n, dp)

    return ans
