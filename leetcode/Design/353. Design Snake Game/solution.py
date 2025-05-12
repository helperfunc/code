class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([[0,0]])
        self.snake_set = set([(0, 0)])
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.directions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    def move(self, direction: str) -> int:
        x, y = self.snake[-1]
        nx, ny = x + self.directions[direction][0], y + self.directions[direction][1]
        if not(-1 < nx < self.height and -1 < ny < self.width):
            return -1
        if (nx, ny) in self.snake_set and [nx, ny] != self.snake[0]:
            # the last status tail is not occupied at this step
            return -1
        eat = self.food[self.food_index] if self.food_index < len(self.food) else None
        
        if eat and eat == [nx, ny]:
            if [nx, ny] == self.snake[0]:
                return -1
            self.food_index += 1
        else:
            if len(self.snake):
                tx, ty = self.snake.popleft()
                self.snake_set.remove((tx, ty))
        self.snake.append([nx, ny])
        self.snake_set.add((nx, ny))
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
