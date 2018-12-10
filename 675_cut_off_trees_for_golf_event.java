class Solution {
    private int row;
    private int col;
    public int cutOffTree(List<List<Integer>> forest) {
        row = forest.size();
        col = forest.get(0).size();
        // trees <[v, x, y]> : < value, x, y index >
        List<int[]> trees = new ArrayList<>();
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j ++) {
                int v = forest.get(i).get(j);
                if (v > 1) {
                    trees.add(new int[]{v, i, j});
                }
            }
        }
        
        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0]));
        
        int ans = 0, sx = 0, sy = 0;
        
        for (int[] tree : trees) {
            int height = tree[0];
            int tx = tree[1]; // tree x
            int ty = tree[2]; // tree y
            int d = dist(forest, sx, sy, tx, ty);
            if (d < 0) {
                return -1;
            }
            ans += d;
            sx = tx;
            sy = ty;
        }
        return ans;
    }
    
    int dist(List<List<Integer>> forest, int sx, int sy, int tx, int ty) {
        boolean[][] visited = new boolean[row][col];
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offerLast(new int[]{sx, sy, 0});// last element is distance
        visited[sx][sy] = true;
        while (!queue.isEmpty()) {
            int[] top = queue.pollFirst();
            int x = top[0];
            int y = top[1];
            int d = top[2];
            // visited[x][y] = true;
            if (x == tx && y == ty) {
                return d;
            }
            
            // for directions:
            if (x + 1 < row && !visited[x + 1][y] && forest.get(x + 1).get(y) > 0) {
                visited[x + 1][y] = true;
                queue.offerLast(new int[]{ x + 1, y, d + 1});
            }
            if (x - 1 >= 0 && !visited[x - 1][y] && forest.get(x - 1).get(y) > 0) {
                visited[x - 1][y] = true;
                queue.offerLast(new int[]{ x - 1, y, d + 1});
            }
            if (y + 1 < col && !visited[x][y + 1] && forest.get(x).get(y + 1) > 0) {
                visited[x][y + 1] = true;
                queue.offerLast(new int[]{ x, y + 1, d + 1});
            }
            if (y - 1 >= 0 && !visited[x][y - 1] && forest.get(x).get(y - 1) > 0) {
                visited[x][y - 1] = true;
                queue.offerLast(new int[]{ x, y - 1, d + 1});
            }
        }
        return -1;
    }
}

