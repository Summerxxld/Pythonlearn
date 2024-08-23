def is_possible(n, tiles):
    def can_place(grid, tile, pos):
        i, j = pos
        top, right, bottom, left = tile
        
        if j > 0:  # Check left neighbor
            left_neighbor = grid[i][j-1]
            if left_neighbor is not None and left_neighbor[1] != left:
                return False
        
        if i > 0:  # Check top neighbor
            top_neighbor = grid[i-1][j]
            if top_neighbor is not None and top_neighbor[2] != top:
                return False
        
        return True

    def backtrack(grid, tiles, index):
        if index == n * n:
            return True
        
        i, j = divmod(index, n)
        
        for tile in tiles:
            if tile not in used:
                if can_place(grid, tile, (i, j)):
                    grid[i][j] = tile
                    used.add(tile)
                    if backtrack(grid, tiles, index + 1):
                        return True
                    grid[i][j] = None
                    used.remove(tile)
        
        return False

    if n == 0:
        return "Impossible"
    
    grid = [[None] * n for _ in range(n)]
    used = set()
    
    return "Possible" if backtrack(grid, tiles, 0) else "Impossible"

def main():
    import sys
    
    game_number = 1
    
    while True:
        n = int(input())
        if n == 0:
            break
        
        tiles = []
        for _ in range(n * n):
            tiles.append(tuple(map(int, input().split())))
        
        result = is_possible(n, tiles)
        print(f"Game {game_number}: {result}\n")
        game_number += 1

if __name__ == "__main__":
    main()
