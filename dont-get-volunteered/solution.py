
dimension = 8

def position_to_coord(pos):
    """
    >>> position_to_coord(0)
    (0, 0)
    >>> position_to_coord(63)
    (7, 7)
    >>> position_to_coord(5)
    (0, 5)
    >>> position_to_coord(-1) is None
    True
    """    
    if 0 <= pos < (dimension ** 2):
        return divmod(pos, dimension)
    return

def coord_exists(row, col):
    """
    >>> coord_exists(8, 8)
    False
    >>> coord_exists(7, 8)
    False
    >>> coord_exists(-1, 4)
    False
    >>> coord_exists(1, 1)
    True
    """
    if 0 <= row < dimension:
        return 0 <= col < dimension
    return False

def coord_to_position(row, col):
    """
    >>> coord_to_position(0, 0)
    0
    >>> coord_to_position(7, 7)
    63
    >>> coord_to_position(0, 5)
    5
    """
    return row * dimension + col


dirs = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1)
    }

def step_(direction, position):
    """
    >>> pos = 27
    >>> step_("UL", pos)
    10
    >>> step_("RD", pos)
    37
    >>> pos = 0
    >>> step_("UL", pos) is None
    True
    """
    cur_row, cur_col = position_to_coord(position)
    for i, letter in enumerate(list(direction)):
        cur_row += (2 - i) * dirs[letter][0]
        cur_col += (2 - i) * dirs[letter][1]

    if not coord_exists(cur_row, cur_col):
        return
    return coord_to_position(cur_row, cur_col)

def solution(current, end):
    """
    >>> solution(0, 1)
    3
    >>> solution(19, 36)
    1
    """
    if current == end:
        return 0
    i = 0
    latest_steps = [current]
    dirs = ["UL","UR","DL","DR","LU","LD","RU","RD"]
    while True:
        i += 1
        new_steps = []
        for pos in set(latest_steps):
            if pos is None:
                continue
            for d in dirs:
                new_step = step_(d, pos)
                if new_step == end:
                    return i
                new_steps.append(new_step)
        latest_steps = new_steps

    

if __name__ == "__main__":
    print(solution(19, 36))
    print(solution(0, 1))
    




