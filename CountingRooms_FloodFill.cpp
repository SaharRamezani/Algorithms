#include <iostream>
#include <vector>
#include <queue>

void floodFill(int i, int j, std::vector<std::vector<char>>& grid) {
    if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == '#' || grid[i][j] == 'v') return;
    grid[i][j] = 'v';
    floodFill(i+1, j, grid);
    floodFill(i-1, j, grid);
    floodFill(i, j+1, grid);
    floodFill(i, j-1, grid);
}

int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<char>> grid(n, std::vector<char>(m));
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            std::cin >> grid[i][j];
        }
    }
    
    int rooms = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(grid[i][j] == '.') {
                floodFill(i, j, grid);
                rooms++;
            }
        }
    }
    
    std::cout << rooms << std::endl;
    return 0;
}
