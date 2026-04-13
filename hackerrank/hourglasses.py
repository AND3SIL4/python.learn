def get_submatrix(matrix, row_init, row_end, col_init, col_end) -> list[list]:
    # Base on its location return a submatrix required
    return [row[col_init:col_end] for row in matrix[row_init:row_end]]


def sum_submatrix(submatrix) -> int:
    # All the matrix are 3x3
    # In the middle row, we only have to sum the middle value
    # Whatever the value would be
    return sum(submatrix[0]) + submatrix[1][1] + sum(submatrix[2])


def hourglassSum(arr) -> int:
    # Define the submatrix length
    lengt_submatrix = 3
    # Create a vector to store the values of each submatrix
    results = []
    for row_index, row in enumerate(arr):
        for col_idx, col in enumerate(row):
            submatrix = get_submatrix(
                arr,
                row_index,
                row_index + lengt_submatrix,
                col_idx,
                col_idx + lengt_submatrix,
            )
            if len(submatrix) == 3 and len(submatrix[0]) == 3:
                total = sum_submatrix(submatrix)
                results.append(total)
    return max(results)


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(hourglassSum(arr=matrix))
