def hourglassSum(arr):
    # Iterate over the array and gets the rows
    # Get the length of the row and initialize the start index
    # length = len(arr[0]) - 1
    # hourglasses_matrix = []
    # for row in arr:
    #     hourglass = []
    #     for i in range(length):
    #         for _ in range(3):
    #             hourglass.append(row[i : i + 3])
    #             print(row[i : i + 3])

    #         print()

    # print(len(hourglasses_matrix))
    tres_filas = arr[0:3:]
    print(tres_filas[0][1:4])


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
