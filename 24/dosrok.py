f = open('dosrok.txt')

n = int(f.readline())


heights = []
for i in range(n):
    height = int(f.readline())
    heights.append(height)


heights.sort()

max_boxes = 0
max_smallest_box = 0
for start_idx in range(n):
    # Try each box as the smallest one
    smallest_box = heights[start_idx]
    current_box = smallest_box
    count = 1
    
    # Try to nest as many boxes as possible
    for j in range(start_idx + 1, n):
        if heights[j] >= current_box + 9:
            current_box = heights[j]
            count += 1
    
    # Update if we found more boxes
    if count > max_boxes:
        max_boxes = count
        max_smallest_box = smallest_box
    # If same number of boxes but larger smallest box
    elif count == max_boxes and smallest_box > max_smallest_box:
        max_smallest_box = smallest_box

print(max_boxes, max_smallest_box)

f.close()