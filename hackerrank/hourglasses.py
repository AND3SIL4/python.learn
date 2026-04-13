def hourglassSum(arr) -> int:
    # Define size of the matrix
    # Matrix cols length
    # Martix rows length
    rows = len(arr)
    cols = len(arr[0])
    # Create a variable to store the max value
    max_value = 0

    # Iterate over the length of the rows
    for i in range(rows - 2):
        # Iterate over the length of the cols
        for j in range(cols - 2):
            # Calculate the sum of the values simulating a submatrix
            total = (
                ((arr[i][j]) + (arr[i][j + 1]) + arr[i][j + 2])
                + (arr[i + 1][j + 1])
                + ((arr[i + 2][j]) + (arr[i + 2][j + 1]) + (arr[i + 2][j + 2]))
            )
            # Replace the current value with the total calculated
            if total > max_value:
                max_value = total
    return max_value  # Return result


if __name__ == "__main__":
    matrix = [
        [0, -4, -6, 0, -7, -6],
        [-1, -2, -6, -8, -3, -1],
        [-8, -4, -2, -8, -8, -6],
        [-3, -1, -2, -5, -7, -4],
        [-3, -5, -3, -6, -6, -6],
        [-3, -6, 0, -8, -6, -7],
    ]
    print(hourglassSum(arr=matrix))
