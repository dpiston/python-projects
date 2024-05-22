n = 9

def main():
	board =[
	[0,0,0,5,0,0,0,0,4],
	[0,0,0,0,2,0,1,8,0],
	[0,0,5,0,7,0,0,0,2],
	[0,0,0,0,3,2,0,0,0],
	[2,0,0,1,0,0,7,5,3],
	[0,0,0,7,4,0,0,0,0],
	[6,7,0,9,8,0,0,0,1],
	[0,0,1,0,0,0,0,4,9],
	[0,4,9,0,0,3,0,0,0]
	]
	
	print_board(board)
	print("")
	solve(board)
	print("")
	print_board(board)

def print_board(board):
	print("| - - - - - - - - - - - |")
	for x in range(n):
		for y in range(n):
			if y == 0:
				print("| ", end="")
			print(f"{board[x][y]} ", end="")
			if y == 8:
				print("|")
			elif (y + 1) % 3 == 0:
				print("| ", end="")
			if (x + 1) % 3 == 0 and y == 8:
				print("| - - - - - - - - - - - |")


def solve(board):
	empty = find_empty(board)
	if not empty:
		return True
	
	for i in range(1, n+1):
		if valid(board, empty, i):
			board[empty[0]][empty[1]] = i
			if solve(board):
				return True
			board[empty[0]][empty[1]] = 0
	return False
		


def find_empty(board):
	for x in range(n):
		for y in range(n):
			if board[x][y] == 0:
				return x, y
	return None


def valid(board, pos, num):
	for x in range(n):
		if board[x][pos[1]] == num:
			return False
	for y in range(n):
		if board[pos[0]][y] == num:
			return False
	start_x = pos[0] - pos[0] % 3
	start_y = pos[1] - pos[1] % 3
	for x in range(3):
		for y in range(3):
			if board[start_x + x][start_y + y] == num:
				return False
	return True


if __name__ == "__main__":
	main()