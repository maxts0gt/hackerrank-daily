def solve_a_maze(maze, start, goal):
    row_len = len(maze)
    col_len = len(maze[0])
    directions = ["UP", "LEFT", "DOWN", "RIGHT"]
    current = start
    current_facing = "UP"
    next = [current[0] - 1, current[1]]
    right = [current[0], current[1] + 1]

    def find_next():
        if current_facing == "UP":
            return [current[0] - 1, current[1]]
        elif current_facing == "DOWN":
            return [current[0] + 1, current[1]]
        elif current_facing == "RIGHT":
            return [current[0], current[1] + 1]
        elif current_facing == "LEFT":
            return [current[0], current[1] - 1]

    def find_right():
        if current_facing == "UP":
            return [current[0], current[1] + 1]
        elif current_facing == "DOWN":
            return [current[0], current[1] - 1]
        elif current_facing == "RIGHT":
            return [current[0] + 1, current[1]]
        elif current_facing == "LEFT":
            return [current[0] - 1, current[1]]

    def turn_left():
        current_facing = directions[directions.index(
            current_facing) + 1 % len(directions)]

    def turn_right():
        current_facing = directions[(directions.index(
            current_facing) - 1 + len(directions)) % len(directions)]

    def move_forward():
        current = next
        next = find_next(current, current_facing)
        right = find_right(current, current_facing)

    left_turn_count = 0
    move_count = 0
    while current != goal:
        right = find_right()
        next = find_next()
        move_count += 1
        if (right[0] < row_len and right[1] < col_len and maze[right[0]][right[1]] == "."):
            turn_right()
            move_forward()
            left_turn_count = 0
        elif (next[0] < row_len and next[1] < col_len and maze[next[0]][next[1]] == "."):
            move_forward()
            left_turn_count = 0
        elif left_turn_count < 4:
            turn_left()
            left_turn_count += 1
        else:
            return -1

    return move_count