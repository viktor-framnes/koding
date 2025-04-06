#chatgpt
tall = [3, 4, 1, 2, 5]
n = len(tall)

for i in range(n // 2):
    # Initialize the min and max positions
    min_idx = i
    max_idx = i

    # Traverse the list from both sides
    for j in range(i, n - i):
        if tall[j] < tall[min_idx]:
            min_idx = j
        if tall[j] > tall[max_idx]:
            max_idx = j

    # Swap the smallest element with the element at the current position
    tall[i], tall[min_idx] = tall[min_idx], tall[i]
    
    # If the largest element was swapped with the smallest, adjust max_idx
    if max_idx == i:
        max_idx = min_idx

    # Swap the largest element with the element at the corresponding end position
    tall[n - i - 1], tall[max_idx] = tall[max_idx], tall[n - i - 1]

print(tall)
