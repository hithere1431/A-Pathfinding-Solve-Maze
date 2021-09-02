from maze import Maze
import heapq as hq

class aStarPathfinding:

    def __init__(self, HEIGHT, WIDTH):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.maze = Maze(HEIGHT, WIDTH)
        self.visited = [[False for i in range(WIDTH)] for i in range(HEIGHT)]
        self.parent = [[(None, None) for i in range(WIDTH)] for i in range(HEIGHT)]

    def printMaze(self, path=None):
        self.maze.printMaze(path)

    def calculateHeuristic(self, i, j):
        return (self.WIDTH - j - 1) + (self.HEIGHT - i - 1)

    def generateNeighbors(self, i, j, visited):
        neighbors = []
        if i-1 >= 0 and visited[i-1][j] == False and self.maze.maze[i][j].n == False and self.maze.maze[i-1][j].s == False: 
            neighbors.append(['n', i-1, j])
        if i+1 < self.HEIGHT and visited[i+1][j] == False and self.maze.maze[i][j].s == False and self.maze.maze[i+1][j].n == False: 
            neighbors.append(['s', i+1, j])
        if j-1 >= 0 and visited[i][j-1] == False and self.maze.maze[i][j].w == False and self.maze.maze[i][j-1].e == False: 
            neighbors.append(['w', i, j-1])
        if j+1 < self.WIDTH and visited[i][j+1] == False and self.maze.maze[i][j].e == False and self.maze.maze[i][j+1].w == False: 
            neighbors.append(['e', i, j+1])
        return neighbors

    def printMaze(self, path):
        ret = ''
        for i in range(self.HEIGHT):
            l1, l2, l3 = '', '', ''
            for j in range(self.WIDTH):
                l1 += '###' + ('###' if self.maze.maze[i][j].n else '   ') + '###'
                l2 += ('###' if self.maze.maze[i][j].w else '   ') + ' ' + ('@' if path[i][j] else ' ') + ' ' + ('###' if self.maze.maze[i][j].e else '   ')
                l3 += '###' + ('###' if self.maze.maze[i][j].s else '   ') + '###'
            ret += l1 + '\n' + l2 + '\n' + l3 + '\n'
        print(ret)

    def solve(self):
        frontier = [(self.calculateHeuristic(0, 0), 0, 0, 0)]
        while len(frontier):
            c, i, j, s = hq.heappop(frontier)
            self.visited[i][j] = True
            neighbors = self.generateNeighbors(i, j, self.visited)
            for neighbor in neighbors:
                frontier.append((self.calculateHeuristic(neighbor[1], neighbor[2]) + s + 1, neighbor[1], neighbor[2], s + 1))
                self.parent[neighbor[1]][neighbor[2]] = (i, j)
            frontier = list(set(frontier))
            
        path = [[False for i in range(self.WIDTH)] for i in range(self.HEIGHT)]
        prev_i, prev_j = self.HEIGHT - 1, self.WIDTH - 1
        path[prev_i][prev_j] = True
        while True:
            next_i, next_j = self.parent[prev_i][prev_j][0], self.parent[prev_i][prev_j][1]
            if next_i == None and next_j == None: break
            else: 
                path[next_i][next_j] = True
                prev_i, prev_j = next_i, next_j
        self.printMaze(path)


x = int(input('Width:'))
y = int(input('Height:'))
solver = aStarPathfinding(y, x)
solver.solve()
