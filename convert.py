import cv2
import sys

image_path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

# load image
img = cv2.imread(image_path, 0)

# edge detection
edges = cv2.Canny(img, 100, 200)

# resize to drawing area
edges = cv2.resize(edges, (width, height))

# find continuous contours instead of pixels
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

coords = []

for contour in contours:

    # simplify contour so it doesn't follow every pixel bump
    epsilon = 1.5
    approx = cv2.approxPolyDP(contour, epsilon, False)

    first = True

    for point in approx:
        x, y = point[0]

        if first:
            coords.append(("DOWN", x, y))
            first = False

        coords.append(("MOVE", x, y))

    if not first:
        coords.append(("UP", x, y))

# save instructions
with open("coords.txt", "w") as f:
    for action, x, y in coords:
        f.write(f"{action},{x},{y}\n")