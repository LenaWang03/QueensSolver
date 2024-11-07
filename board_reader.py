import cv2 as cv
import numpy as np
import math
from board_solver import solve


# Load the image
original = cv.imread('board.png')

# crop the image so its just the board
gray_board = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
contours, _ = cv.findContours(gray_board, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv.contourArea, reverse=True)
# get dimensions of the board
x, y, w, h = cv.boundingRect(contours[1])
# crop
grid = original[y:y+h, x:x+w]
gray = cv.cvtColor(grid, cv.COLOR_BGR2GRAY)
cv.imwrite("gray-grid.png", gray)

# store the board layout in a 2D array
contours, _ = cv.findContours(gray_board, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv.contourArea)
total_cells = len(contours) - 2
print("Total cells detected:", total_cells)
grid_size = int(math.sqrt(total_cells))
if total_cells != grid_size**2:
    print("Unable to detect full grid! Aborting")
cell_width = w // grid_size
cell_height = h // grid_size
colors = []
board = []
color_index = 1
color_map = {}
reverse_color_map = {}
padding = 10
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        # calculate cell coordinates
        cell_x = j * cell_width
        cell_y = i * cell_height

        padding = 15
        cell = grid[cell_y+padding:cell_y+cell_height-padding, cell_x+padding:cell_x+cell_width-padding]
        
        # get the average color of the cell
        avg_color = cell.mean(axis=0).mean(axis=0)
        avg_color = avg_color.astype(int)
        avg_color = tuple(avg_color)
        
        # append the color in RGB format
        if avg_color not in color_map:
            color_map[avg_color] = str(color_index)
            reverse_color_map[str(color_index)] = avg_color
            color_index += 1
        row.append(color_map[avg_color])
        
    board.append(row)

solve(board)
# Print the board to the console
for row in board:
    print(row)