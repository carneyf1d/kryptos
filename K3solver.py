def create_transposition_table(input_string, num_columns):
    # Calculate the length of each chunk
    chunk_length = num_columns
    
    # Split the input string into chunks
    chunks = [input_string[i:i + chunk_length] for i in range(0, len(input_string), num_columns)]
    
    # Create the transposition table (list of lists)
    transposition_table = [list(chunk) for chunk in chunks]
    res = []
    for row in transposition_table:
        print(" ".join(row))
    return transposition_table


def rotate_clockwise(matrix):
    """
    Rotates a 2D matrix (table) clockwise by 90 degrees.
    Args:
        matrix (list of lists): The input matrix to be rotated.
    Returns:
        list of lists: The rotated matrix.
    """
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if num_rows > 0 else 0

    # Create an empty rotated matrix with swapped dimensions
    rotated_matrix = [[None] * num_rows for _ in range(num_columns)]

    # Populate the rotated matrix
    for i in range(num_rows):
        for j in range(num_columns):
            rotated_matrix[j][num_rows - i - 1] = matrix[i][j]
    res = []
    for row in rotated_matrix:
        print(" ".join(row))
        text = "".join(row)
        res.append(text)
    return "".join(res)