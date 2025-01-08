from itertools import combinations

# Define the items with their properties
items = [
    {"name": "rifle", "code": "r", "size": 3, "survival_points": 25},
    {"name": "pistol", "code": "p", "size": 2, "survival_points": 15},
    {"name": "ammo", "code": "a", "size": 2, "survival_points": 15},
    {"name": "medkit", "code": "m", "size": 2, "survival_points": 20},
    {"name": "inhaler", "code": "i", "size": 1, "survival_points": 5},
    {"name": "knife", "code": "k", "size": 1, "survival_points": 15},
    {"name": "axe", "code": "x", "size": 3, "survival_points": 20},
    {"name": "talisman", "code": "t", "size": 1, "survival_points": 25},
    {"name": "flask", "code": "f", "size": 1, "survival_points": 15},
    {"name": "antidot", "code": "d", "size": 1, "survival_points": 10},
    {"name": "supplies", "code": "s", "size": 2, "survival_points": 20},
    {"name": "crossbow", "code": "c", "size": 2, "survival_points": 20},
]

# Constants
BACKPACK_CAPACITY = 8  # 2x4 backpack
initial_points = 10

# Filter mandatory item "antidot"
mandatory_item = next(item for item in items if item["code"] == "d")

# Function to calculate inventory score and validate size
def evaluate_combination(combination):
    total_size = sum(item["size"] for item in combination)
    total_points = sum(item["survival_points"] for item in combination) + initial_points
    return total_size <= BACKPACK_CAPACITY and total_points > 0, total_points

# Generate all possible combinations excluding mandatory item, add it back
valid_combinations = []
for r in range(1, len(items)):
    for combination in combinations(items, r):
        if mandatory_item not in combination:
            continue
        valid, score = evaluate_combination(combination)
        if valid:
            valid_combinations.append((combination, score))

# Find the best combination based on survival points
best_combination, best_score = max(valid_combinations, key=lambda x: x[1])

# Fill the backpack grid
backpack = []
for item in best_combination:
    backpack.extend([item["code"]] * item["size"])

# Format backpack into 2x4 grid
grid = [backpack[i:i+4] for i in range(0, len(backpack), 4)]

print(grid, best_score)