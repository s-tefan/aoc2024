from collections import Counter

def blink_stones(stones_counter):
    new_stones_counter = Counter()
    
    for stone, count in stones_counter.items():
        # Rule 1: If the stone is 0, it becomes 1
        if stone == 0:
            new_stones_counter[1] += count
        else:
            stone_str = str(stone)
            # Rule 2: If the number has an even number of digits, split it
            if len(stone_str) % 2 == 0:
                half = len(stone_str) // 2
                left = int(stone_str[:half])
                right = int(stone_str[half:])
                new_stones_counter[left] += count
                new_stones_counter[right] += count
            else:
                # Rule 3: Otherwise, multiply the stone's number by 2024
                new_stones_counter[stone * 2024] += count
    
    return new_stones_counter

def count_stones_after_blinks(stones, num_blinks):
    # Initial counter for the stones
    stones_counter = Counter(stones)
    
    for _ in range(num_blinks):
        stones_counter = blink_stones(stones_counter)
    
    # The number of stones is the sum of all counts in the counter
    return sum(stones_counter.values())

# Sample input: Let's start with the example from the problem
initial_stones = [125, 17]

# Run the simulation for 75 blinks
result = count_stones_after_blinks(initial_stones, 75)

print(f"Number of stones after 75 blinks: {result}")
