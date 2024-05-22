# python-projects
Some Various projects I have made or am working on in C++.

### Price Tracker


### Sudoku
A sudoku puzzle solver utlizing CV2 and numpy, very purpose built and runs on my phone. Works with the [Easybrain Sudoku App](https://play.google.com/store/apps/details?id=com.easybrain.sudoku.android&hl=en_US&gl=US&pli=1).
-**Search for Sudoku Screenshots**: The program searches for Sudoku screenshots in the screenshot folder on your phone.

-**Move Files**: It moves the detected screenshot files to its local file tree for processing.

-**Detect Sudoku Board**: Using contours, the program identifies the Sudoku board within the screenshot.

-**Zoom In on the Board**: It zooms in on the detected board to focus on the puzzle grid.

-**Recognize Numbers**: Leveraging pre-saved templates of numbers, the program loops through the rows and columns of the board, saving the detected integers into a 9x9 array. Empty spots are represented by 0s.

-**Solve the Puzzle**: The 9x9 array is passed to a solving algorithm, which returns a solved array.

-**Generate Solution Array**: The program compares the solved array with the initial array. Pre-given numbers are converted to 0s, and the solved numbers are placed in the previously empty spots.

-**Transpose Numbers onto the Board**: Finally, the solved numbers are transposed onto the blank spots in the zoomed-in board image, creating a completed puzzle.
