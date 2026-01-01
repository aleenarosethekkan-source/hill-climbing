import random
import time

def generate_map(width, height, max_height):
    """Generates a 2D map with random altitudes."""
    return [[random.randint(0, max_height) for _ in range(width)] for _ in range(height)]

def print_map(game_map, path):
    """Prints the map, highlighting the player's path."""
    path_points = set(path)
    for r, row in enumerate(game_map):
        for c, cell in enumerate(row):
            if (r, c) in path_points:
                if (r,c) == path[-1]:
                    print(f"⛰️{cell:2d}", end=" ")  # Peak as a mountain emoji
                else:
                    print(f"\x1b[32m{cell:2d}\x1b[0m", end=" ") # Path in green
            else:
                print(f"{cell:2d}", end=" ")
        print()

def get_neighbors(game_map, r, c):
    """Gets the valid neighbors of a cell."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(game_map) and 0 <= nc < len(game_map[0]):
                neighbors.append((nr, nc))
    return neighbors

def hill_climb(game_map, start_r, start_c):
    """Performs the hill climbing algorithm."""
    path = [(start_r, start_c)]
    r, c = start_r, start_c
    while True:
        neighbors = get_neighbors(game_map, r, c)
        current_height = game_map[r][c]
        best_neighbor = None
        max_height = current_height

        for nr, nc in neighbors:
            if game_map[nr][nc] > max_height:
                max_height = game_map[nr][nc]
                best_neighbor = (nr, nc)

        if best_neighbor:
            r, c = best_neighbor
            path.append((r, c))
        else:
            return path # Reached a peak

def main():
    """Main function to run the game."""
    width = 20
    height = 10
    max_height = 99

    print("Generating map...")
    game_map = generate_map(width, height, max_height)

    start_r = random.randint(0, height - 1)
    start_c = random.randint(0, width - 1)

    print(f"Starting at ({start_r}, {start_c})")
    print("Finding path to peak...")

    path = hill_climb(game_map, start_r, start_c)

    print("\n--- Map ---")
    print_map(game_map, path)
    print("\n--- Results ---")
    print(f"Path taken: {path}")
    print(f"Peak found at: {path[-1]} with height {game_map[path[-1][0]][path[-1][1]]}")

if __name__ == "__main__":
    main()
