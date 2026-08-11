def max_web_strike(grid, m):
    n = len(grid)
    r = m // 2

    best_count = -1
    best_row, best_col = -1, -1


    for row in range(r, n - r):
        for col in range(r, n - r):
            if grid[row][col] != 1:
                continue

            count = 0
            for i in range(row - r, row + r + 1):
                for j in range(col - r, col + r + 1):
                    count += grid[i][j]

            if count > best_count:
                best_count = count
                best_row, best_col = row, col

    if best_count == -1:
        return None, 0, []
    
    best_x = best_col
    best_y = n - 1 - best_row

    criminals = []
    for i in range(best_row - r, best_row + r + 1):
        for j in range(best_col - r, best_col + r + 1):
            if grid[i][j] == 1:
                cx = j
                cy = n - 1 - i
                criminals.append((cx, cy))

    return (best_x, best_y), best_count, criminals

if __name__ == "__main__":
    grid = [
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1],
    ]
    m = 3

    coord, count, criminals = max_web_strike(grid, m)
    print("Best launch coordinate:", coord)
    print("Maximum criminals captured:", count)
    print("Criminal coordinates in region:", sorted(criminals))
