import heapq

def misplaced(state, goal):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


def manhattan(state, goal):
    distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:

                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == state[i][j]:
                            distance += abs(i - x) + abs(j - y)

    return distance


def a_star(initial, goal, heuristic):

    open_list = []
    visited = set()

    h = heuristic(initial, goal)

    # (f, g, state, path)
    heapq.heappush(open_list, (h, 0, initial, []))

    moves = [(-1, 0, "Up"),
             (1, 0, "Down"),
             (0, -1, "Left"),
             (0, 1, "Right")]

    while open_list:

        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return g, path + [state]

        state_tuple = tuple(tuple(row) for row in state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # Find blank
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        for dx, dy, move in moves:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:

                new_state = [row[:] for row in state]

                new_state[x][y], new_state[nx][ny] = \
                    new_state[nx][ny], new_state[x][y]

                new_tuple = tuple(tuple(row) for row in new_state)

                if new_tuple not in visited:

                    new_g = g + 1
                    new_h = heuristic(new_state, goal)
                    new_f = new_g + new_h

                    heapq.heappush(
                        open_list,
                        (new_f, new_g, new_state,
                         path + [state])
                    )

    return None


initial = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Case 1: Misplaced Tiles
cost, solution = a_star(initial, goal, misplaced)

print("Misplaced Tiles")
print("Cost:", cost)

for state in solution:
    for row in state:
        print(row)
    print()


# Case 2: Manhattan Distance
cost, solution = a_star(initial, goal, manhattan)

print("Manhattan Distance")
print("Cost:", cost)

for state in solution:
    for row in state:
        print(row)
    print()
