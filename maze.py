from dataclasses import dataclass
import random

@dataclass
class Cell:
    n: bool
    s: bool
    w: bool
    e: bool

class Maze:

    def __init__(self, HEIGHT, WIDTH):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.maze = [[Cell(True, True, True, True) for i in range(WIDTH)] for i in range(HEIGHT)]
        self.visited = [[False for i in range(WIDTH)] for i in range(HEIGHT)]
        self.generateMaze()

    def generateNeighbors(self, i, j, visited):
        neighbors = []
        if i-1 >= 0 and visited[i-1][j] == False: neighbors.append(['n', i-1, j])
        if i+1 < self.HEIGHT and visited[i+1][j] == False: neighbors.append(['s', i+1, j])
        if j-1 >= 0 and visited[i][j-1] == False: neighbors.append(['w', i, j-1])
        if j+1 < self.WIDTH and visited[i][j+1] == False: neighbors.append(['e', i, j+1])
        return neighbors

    def removeWall(self, i, j, direction):
        if direction == 'n': self.maze[i][j].n, self.maze[i-1][j].s= False, False
        elif direction == 's': self.maze[i][j].s, self.maze[i+1][j].n= False, False
        elif direction == 'w': self.maze[i][j].w, self.maze[i][j-1].e= False, False
        elif direction == 'e': self.maze[i][j].e, self.maze[i][j+1].w= False, False

    def generateMaze(self):
        i = random.randint(0, self.HEIGHT-1)
        j = random.randint(0, self.WIDTH-1)
        frontier = []
        while True:
            self.visited[i][j] = True
            neighbors = self.generateNeighbors(i, j, self.visited)
            random.shuffle(neighbors)
            if len(neighbors) == 0:
                if len(frontier): i, j = frontier.pop()
                else: break
            else:
                self.removeWall(i, j, neighbors[0][0])
                frontier.append((i, j))
                i, j = neighbors[0][1], neighbors[0][2]
        self.maze[0][0].w = False
        self.maze[self.HEIGHT-1][self.WIDTH-1].e = False
    

