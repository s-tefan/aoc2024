def blink_stones(stones):
    new_stones = []
    
    for stone in stones:
        # Rule 1: If the stone is 0, it becomes 1
        if stone == 0:
            new_stones.append(1)
        else:
            stone_str = str(stone)
            # Rule 2: If the number has an even number of digits, split it
            if len(stone_str) % 2 == 0:
                half = len(stone_str) // 2
                left = int(stone_str[:half])
                right = int(stone_str[half:])
                new_stones.append(left)
                new_stones.append(right)
            else:
                # Rule 3: Otherwise, multiply the stone's number by 2024
                new_stones.append(stone * 2024)
    
    return new_stones

def count_stones_after_blinks(stones, num_blinks):
    for _ in range(num_blinks):
        stones = blink_stones(stones)
    return len(stones)

# Sample input: Let's start with the example from the problem
initial_stones = initial_stones = [125, 17]


# Run the simulation for 25 blinks
result = count_stones_after_blinks(initial_stones, 25)

print(f"Number of stones after 25 blinks: {result}")
