# def print_grid(grid):
#     print()
#     print(*grid, sep="\n")
#     print()


def poutine_path(r: int, c: int, m: tuple[tuple[int, ...]]) -> int:
    dp = [[-1 for _ in range(c)] for _ in range(r)]

    dp[r - 1][0] = m[r - 1][0]

    for i in range(r - 2, -1, -1):
        dp[i][0] = m[i][0] + dp[i + 1][0]

    for j in range(1, c):
        dp[r - 1][j] = m[r - 1][j] + dp[r - 1][j - 1]

    for j in range(1, c):
        for i in range(r - 2, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + m[i][j]

    return dp[0][c - 1]


# def poutine_path2(r: int, c: int, m: tuple[tuple[int, ...]]) -> int:

#     def is_inside(i: int, j: int) -> bool:
#         return 0 <= i < r and 0 <= j < c

#     location: list[int] = [r - 1, 0]
#     target: list[int] = [0, c - 1]

#     max_rubles: int = -1

#     def go_up(location: list[int], curr_rubles: int) -> None:
#         nonlocal max_rubles
#         i, j = location
#         new_i, new_j = i - 1, j

#         if location == target:
#             if curr_rubles > max_rubles:
#                 max_rubles = curr_rubles
#             return

#         if is_inside(new_i, new_j):
#             curr_rubles += m[new_i][new_j]
#         else:
#             return

#         go_up([new_i, new_j], curr_rubles)
#         go_right([new_i, new_j], curr_rubles)

#     def go_right(location: list[int], curr_rubles: int) -> None:
#         nonlocal max_rubles
#         i, j = location
#         new_i, new_j = i, j + 1

#         if location == target:
#             if curr_rubles > max_rubles:
#                 max_rubles = curr_rubles
#             return

#         if is_inside(new_i, new_j):
#             curr_rubles += m[new_i][new_j]
#         else:
#             return

#         go_up([new_i, new_j], curr_rubles)
#         go_right([new_i, new_j], curr_rubles)

#     def backtracking():
#         i, j = location

#         go_up([i, j], m[i][j])

#         i, j = location
#         go_right([i, j], m[i][j])

#         ans = max_rubles
#         return ans

#     return backtracking()


# def poutine_path3(r: int, c: int, m: tuple[tuple[int, ...]]) -> int:
#     dp = list(list(num for num in row) for row in m)
#     print_grid(dp)

#     def vertical_edge(i: int, grid: list[list[int]]) -> list[list[int]]:
#         def _help_v(ii) -> int:
#             if ii == r - 1:
#                 return dp[r - 1][0]
#             grid[ii][0] = dp[ii][0] + _help_v(ii + 1)
#             return grid[ii][0]

#         _help_v(i)

#         return grid

#     def horizontal_edge(j: int, grid: list[list[int]]):
#         def _help_h(jj):
#             if jj == 0:
#                 return dp[r - 1][0]
#             grid[r - 1][jj] = dp[r - 1][jj] + _help_h(jj - 1)
#             return grid[r - 1][jj]

#         _help_h(j)

#         return grid

#     dp = vertical_edge(0, dp)
#     print_grid(dp)
#     dp = horizontal_edge(c - 1, dp)
#     print_grid(dp)
    
#     def solve(i, j, grid):
#         def _help_s(ii, jj):
#             if ii == r - 1:
#                 return dp[r - 1][jj]
            
#             if jj == 0:
#                 return dp[ii][0]
            
#             grid[ii][jj] = max(_help_s(ii + 1, jj), _help_s(ii, jj - 1)) + dp[ii][jj]
#             return grid[ii][jj]
            
            
#         _help_s(i, j)
        
#         return grid
        
#     dp = solve(0, c - 1, dp)
    
#     print_grid(dp)
    
#     return dp[0][c-1]