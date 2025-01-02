# Time: O(n*m)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 0):
                    q.append([r,c])

        directions = [[0,+1],[0,-1],[+1,0],[-1,0]]
        
        while(q):
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in directions:
                    row,col = dr + r, dc +c
                    if(row >= 0 and row < rows and
                       col >= 0 and col < cols and
                       grid[row][col] == INF
                      ):
                        q.append([row,col])
                        grid[row][col] = grid[r][c] + 1 # current cell distance + 1
                          