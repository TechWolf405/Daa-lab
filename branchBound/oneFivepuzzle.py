import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return self.depth < other.depth

    def __hash__(self):
        return hash(str(self.puzzle))

    def is_goal(self):
        return self.puzzle.is_solved()

    def generate_children(self):
        children = []
        empty_pos = self.puzzle.find_empty()
        for move in self.puzzle.get_moves(empty_pos):
            new_puzzle = self.puzzle.copy()
            new_puzzle.move(empty_pos, move)
            child = PuzzleState(new_puzzle, self, move)
            children.append(child)
        return children

class Puzzle:
    def __init__(self, puzzle):
        self.size = len(puzzle)
        self.puzzle = puzzle

    def is_solved(self):
        n = self.size
        for i in range(n):
            for j in range(n):
                if self.puzzle[i][j] != i * n + j + 1:
                    return False
        return True

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return (i, j)

    def get_moves(self, empty_pos):
        moves = []
        i, j = empty_pos
        if i > 0:
            moves.append((-1, 0))
        if i < self.size - 1:
            moves.append((1, 0))
        if j > 0:
            moves.append((0, -1))
        if j < self.size - 1:
            moves.append((0, 1))
        return moves

    def move(self, empty_pos, move):
        i, j = empty_pos
        dx, dy = move
        new_i, new_j = i + dx, j + dy
        self.puzzle[i][j], self.puzzle[new_i][new_j] = self.puzzle[new_i][new_j], self.puzzle[i][j]

    def manhattan_distance(self):
        n = self.size
        distance = 0
        for i in range(n):
            for j in range(n):
                value = self.puzzle[i][j]
                if value != 0:
                    goal_i, goal_j = (value - 1) // n, (value - 1) % n
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def copy(self):
        new_puzzle = [row[:] for row in self.puzzle]
        return Puzzle(new_puzzle)

def solve_puzzle(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (initial_state.depth + initial_state.puzzle.manhattan_distance(), initial_state))
    visited = set()

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)
        visited.add(current_state)

        if current_state.is_goal():
            return current_state

        children = current_state.generate_children()
        for child in children:
            if child not in visited:
                heapq.heappush(priority_queue, (child.depth + child.puzzle.manhattan_distance(), child))

    return None

def print_solution(solution_state):
    moves = []
    current_state = solution_state
    while current_state:
        moves.append(current_state.move)
        current_state = current_state.parent
    moves.reverse()
    print("Solution:")
    for move in moves[1:]:
        print(move)

def main():
    puzzle = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 7, 12],
        [13, 14, 11, 15]
    ]
    initial_state = PuzzleState(Puzzle(puzzle))
    solution_state = solve_puzzle(initial_state)
    if solution_state:
        print_solution(solution_state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
