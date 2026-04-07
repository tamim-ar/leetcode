class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0
        self.dirs = ["East", "North", "West", "South"]
        self.moves = [(1,0), (0,1), (-1,0), (0,-1)]
        self.perimeter = 2 * (width + height) - 4
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        num %= self.perimeter
        if num == 0:
            num = self.perimeter
        
        for _ in range(num):
            nx = self.x + self.moves[self.dir][0]
            ny = self.y + self.moves[self.dir][1]
            
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
                nx = self.x + self.moves[self.dir][0]
                ny = self.y + self.moves[self.dir][1]
            
            self.x, self.y = nx, ny

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        if not self.moved:
            return "East"
        return self.dirs[self.dir]