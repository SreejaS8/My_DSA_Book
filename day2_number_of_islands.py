class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    c += 1
        return c
    def dfs(self,grid,i,j):
        try:
            if (i<0 or j<0 or i>=len(grid[0]) or grid[i][j]) != '1':
                return
            grid[i][j] = '#'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
        except IndexError:
            pass

grid = [["1"],["1"]]
print(Solution().numIslands(grid))