class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.foods = []
        for fx, fy in food:
            self.foods.append((fx, fy))
        self.food_index = 0

        self.width = width
        self.height = height
        self.body = [[0,0]]
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head_x, head_y = self.body[0]
        next_x = head_x
        next_y = head_y
        if direction == 'U':
            next_x -= 1
        elif direction == 'L':
            next_y -= 1
        elif direction == 'R':
            next_y += 1
        elif direction == 'D':
            next_x += 1
            
        if next_x >= self.height or next_x < 0 or next_y >= self.width or next_y < 0:
            return -1
        
        self.body.insert(0, [next_x, next_y])

        if self.food_index < len(self.foods) and (next_x, next_y) == self.foods[self.food_index]:
            self.food_index += 1
        else:
            self.body.pop()
        
        for i in range(1, len(self.body)):
            if next_x == self.body[i][0] and next_y == self.body[i][1]:
                return -1

        return len(self.body) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
