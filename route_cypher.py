message = " ".join(str(x) for x in range(16))
key = [1, -2, 3, -4]
rows = 4
collumns = 4


def encrypt(message: str, rows: int, cols: int, order: list) -> str:
    """Encripts a given message.

    Args:
      - message: words separated by spaces.
      - rows: number of rows used in the cypher.
      - cols: number of collumns used in the cypher.
      - order: list in which the columns get put

    Returns:  Encrypted message.
    """
    matrix = [[] for n in range(cols)]
    message = message.split()
    for row in range(rows):
        for col in range(cols):
            matrix[row].append(message[(row*cols)+col])
    final_matrix = [[] for n in range(cols)]

    for n in order:
        if n > 0:
            for x, collumn in enumerate(matrix):
                final_matrix[x].append(collumn[n-1])
        else:
            for x, collumn in enumerate(matrix):
                final_matrix[cols - x - 1].append(collumn[(n + 1) * -1])

    message = ""
    for row in final_matrix:
        message += " ".join(number for number in row) + " "
    return message


print(encrypt(message, rows, collumns, key))
