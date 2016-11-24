def validate_row(row):
    return len(row) == 9 and len(set(row)) == 9 and all(1 <= e <= 9 for e in row)


def validate_rows(matrix):
    result = True
    for row in matrix:
        result = result and validate_row(row)
    return result


def validate_columns(matrix):
    return validate_rows(list(zip(*matrix)))


def validate_tiles(matrix):
    length = int(len(matrix) / 3)

    row_start = 0
    for row_end in range(length, len(matrix) + 1, length):
        col_start = 0
        for col_end in range(length, len(matrix) + 1, length):
            m = list()
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    m.append(matrix[row][col])

            if not validate_row(m):
                return False

            col_start = col_end
        row_start = row_end

    return True


def validate(matrix):
    return validate_rows(matrix) and validate_columns(matrix) and validate_tiles(matrix)
