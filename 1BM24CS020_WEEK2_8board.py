import copy

class EightPuzzle:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.moves = [(-1,0), (1,0), (0,-1), (0,1)]

    def successors(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        result = []
        for dx, dy in self.moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = copy.deepcopy(state)
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                result.append(new)
        return result

    def dfs(self, state, visited):
        if state == self.goal:
            return True

        key = tuple(map(tuple, state))
        visited.add(key)

        for next_state in self.successors(state):
            if tuple(map(tuple, next_state)) not in visited:
                if self.dfs(next_state, visited):
                    return True
        return False

    def dls(self, state, depth):
        if state == self.goal:
            return True
        if depth == 0:
            return False

        for next_state in self.successors(state):
            if self.dls(next_state, depth - 1):
                return True
        return False

    def ids(self):
        depth = 0
        while depth <= 10:
            if self.dls(self.initial, depth):
                print("Goal found at depth", depth)
                return True
            depth += 1
        print("Goal not found")


initial = [[1,2,3], [0,4,6], [7,5,8]]
goal = [[1,2,3], [4,5,6], [7,8,0]]

puzzle = EightPuzzle(initial, goal)

print("DFS:", puzzle.dfs(initial, set()))

print("IDS:")
puzzle.ids()
