import itertools
import heapq

# 33. Find All Permutations of a String
def all_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# 34. N-th Fibonacci Number (Dynamic Programming)
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 35. Find Duplicates in a List
def find_duplicates(lst):
    count = {}
    duplicates = []
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    return duplicates

# 36. Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    lis = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

# 37. Find K Largest Elements
def k_largest_elements(lst, k):
    return heapq.nlargest(k, lst)

# 38. Rotate Matrix 90 Degrees Clockwise
def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

# 39. Sudoku Validator
def is_valid_sudoku(board):
    # Check rows and columns for duplicates
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in row:
                return False
            if board[j][i] != '.' and board[j][i] in col:
                return False
            row.add(board[i][j])
            col.add(board[j][i])

    # Check 3x3 subgrids for duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] != '.' and board[x][y] in subgrid:
                        return False
                    subgrid.add(board[x][y])

    return True

# Main Menu Driven Program
def menu():
    while True:
        print("\nMenu:")
        print("1. Find All Permutations of a String")
        print("2. N-th Fibonacci Number (Dynamic Programming)")
        print("3. Find Duplicates in a List")
        print("4. Longest Increasing Subsequence (LIS)")
        print("5. Find K Largest Elements")
        print("6. Rotate Matrix 90 Degrees Clockwise")
        print("7. Sudoku Validator")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            s = input("Enter a string: ")
            print("All permutations:", all_permutations(s))

        elif choice == '2':
            n = int(input("Enter a number: "))
            print("The", n, "th Fibonacci number is:", fibonacci(n))

        elif choice == '3':
            lst = list(map(int, input("Enter a list of integers: ").split()))
            print("Duplicate elements:", find_duplicates(lst))

        elif choice == '4':
            arr = list(map(int, input("Enter a list of integers: ").split()))
            print("Length of LIS:", longest_increasing_subsequence(arr))

        elif choice == '5':
            lst = list(map(int, input("Enter a list of integers: ").split()))
            k = int(input("Enter the value of k: "))
            print(f"The {k} largest elements are:", k_largest_elements(lst, k))

        elif choice == '6':
            matrix = []
            print("Enter the matrix row by row (separate elements by space):")
            for i in range(3):
                row = list(map(int, input().split()))
                matrix.append(row)
            print("Rotated matrix:")
            for row in rotate_matrix(matrix):
                print(row)

        elif choice == '7':
            board = []
            print("Enter the Sudoku board row by row (use '.' for empty cells):")
            for i in range(9):
                row = input().split()
                board.append(row)
            if is_valid_sudoku(board):
                print("The Sudoku board is valid.")
            else:
                print("The Sudoku board is not valid.")

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu-driven program
if __name__ == "__main__":
    menu()