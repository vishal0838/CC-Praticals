N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

# Arrays for Branch and Bound
column = [False] * N
leftDiagonal = [False] * (2 * N)
rightDiagonal = [False] * (2 * N)


# Function to print board
def print_board():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Function to solve problem
def solve(row):

    # All queens placed
    if row == N:
        print_board()
        return True

    for col in range(N):

        # Check safe position
        if (not column[col] and
            not leftDiagonal[row - col + N] and
            not rightDiagonal[row + col]):

            # Place queen
            board[row][col] = 1

            column[col] = True
            leftDiagonal[row - col + N] = True
            rightDiagonal[row + col] = True

            # Recursive call
            if solve(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

            column[col] = False
            leftDiagonal[row - col + N] = False
            rightDiagonal[row + col] = False

    return False


# Main
solve(0)