import cv2
import numpy as np
import imutils
import copy
import os
import sudoku
import time

def find_board(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	canny = cv2.Canny(gray, 30, 180)
	keys = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(keys)

	contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]
	location = None

	for ct in contours:
		approx = cv2.approxPolyDP(ct, 15, True)
		if len(approx) == 4:
			location = approx
			break

	result = get_perspective(img, location)
	
	return result
	
	
def get_perspective(im, location, height = 900, width = 900):
	pts1 = np.float32([location[0], location[3], location[1], location[2]])
	pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
	
	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	result = cv2.warpPerspective(im, matrix, (width, height))
	return result


def split_boxes(grid):
	st = time.time()
	template = [cv2.imread("One.jpg"), cv2.imread("Two.jpg"), cv2.imread("Three.jpg"), cv2.imread("Four.jpg"), cv2.imread("Five.jpg"), cv2.imread("Six.jpg"), cv2.imread("Seven.jpg"), cv2.imread("Eight.jpg"), cv2.imread("Nine.jpg")]
	boxes = [[0 for i in range(9)] for j in range(9)]
	threshold = .9
	x = 0
	y = 0
	rows = np.vsplit(grid, 9)
	for r in rows:
		cols = np.hsplit(r, 9)
		y = 0
		for box in cols:
			for i in range(len(template)):
				box_img = cv2.imencode(".jpg", box)
				box = cv2.imdecode(box_img[1], cv2.IMREAD_COLOR)
				res = cv2.matchTemplate(box, template[i], cv2.TM_CCOEFF_NORMED)
				check = np.where(res >= threshold)
				if len(check[0]) != 0:
					boxes[x][y] = i + 1
					break
			y += 1
		x += 1
	print(time.time() - st)
	print()
	return boxes


def input_nums(img, nums):
	font = cv2.FONT_HERSHEY_SIMPLEX 
	font_scale = 2
	color = (0, 0, 200)
	thickness = 5
	for x in range(9):
		for y in range(9):
			if nums[x][y] != 0:
				cv2.putText(img, str(nums[x][y]), ( 30 + (100 * y), 70 + (100 * x)), font, font_scale, color, thickness)



if __name__ == "__main__":
	src_path = "/storage/emulated/0/dcim/Screenshots"
	dst_path="/storage/emulated/0/Programming/Python/Sudoku/Boards"
	print("---‐--------------------------------------------")
	print("Welcome to my Sudoku Solver!")
	print("---‐--------------------------------------------")
	print("\n")
	print("Finding any unsolved boards...")
	print("")
	count = 1
	for f in os.listdir(dst_path):
		if "Solved" not in f:
			count += 1

	unsolved = count

	for f in os.listdir(src_path):
		if "Sudoku" in f:
			os.rename(f"{src_path}/{f}", f"{dst_path}/Sudoku_{unsolved}.jpg")
			unsolved += 1

	if unsolved == count:
		print("No unsolved boards found")
		print()
		print("Exiting program")
		exit()
	else:
		print(f"Unsolved boards found: {unsolved - count}")
		print()

	for f in os.listdir(dst_path):
		file, delim = f.split(".")
		if os.path.exists(f"{dst_path}/{file}_Solved.jpg") or "Solved" in f:
			continue
		else:
			print("Isolating board...")
			print()
			board = find_board(cv2.imread(f"Boards/{file}.jpg"))
			board_gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
			
			print("Enumerating boxes...")
			print()
			solve_board = split_boxes(board_gray)
			compare_board = copy.deepcopy(solve_board)
			
			print("Solving board...")
			print()
			sudoku.solve(solve_board)
	
			for row in range(9):
				for col in range(9):
					if compare_board[row][col] != 0:
						solve_board[row][col] = 0
			
			print("Inputing answer...")
			print()
			input_nums(board, solve_board)
	
			print("Saving answer key...")
			print()
	
			cv2.imwrite(f"Boards/{file}_Solved.jpg", board)
			
			print(f"Solved {file}!")
			print()
			
	print("All unsolved boards complete!")