# NOT WORKING

n, m = map(int, input().split())

dp = [[-1 for _ in range(1<<n)] for _ in range(m)]
MOD = 1000000007

def generate_next_masks(row, mask, next_mask, next_masks):
    if row == n:
        next_masks.append(next_mask)
        return

    if mask & 1<<row != 0:
        generate_next_masks(row+1, mask, next_mask, next_masks)
    
    if row != n-1 and (mask & 1<<row == 0) and (mask & 1<<row+1 == 0):
        generate_next_masks(row+2, mask, next_mask, next_masks)

    if (mask & 1<<row == 0):
        generate_next_masks(row+1, mask, next_mask | 1<<row, next_masks)  # Make a copy here

    return

def solve(col, mask):
    if col == m:
        if mask == 0:
            return 1
        return 0

    if dp[col][mask] != -1:
        return dp[col][mask]

    ans = 0

    next_masks = []

    generate_next_masks(0, mask, 0, next_masks)

    for next_mask in next_masks:
        ans = (ans + solve(col+1, next_mask)) % MOD

    dp[col][mask] = ans

    return dp[col][mask]

# current_col, mask
print(solve(0, 0))
