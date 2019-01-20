import java.util.ArrayDeque;
import java.util.Deque;

public class ShortestPathWithBreakings {
    static class Step {
        int[] coordinate;
        int breakings;
        Step(int[] coordinate, int breakings) {
            this.coordinate = coordinate;
            this.breakings = breakings;
        }
    }

    private int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int shortestPathWithOneBreaking(char[][] maze, int[] start, int[] end) {
        int row = maze.length;
        int col = maze[0].length;
        Deque<Step> queue = new ArrayDeque<>();
        queue.offer(new Step(start, 1));
        maze[start[0]][start[1]] = 'X';
        int result = 0;
        while (!queue.isEmpty()) {
            for (int i = 0; i < queue.size(); i++) {
                Step top = queue.poll();
                if (maze[top.coordinate[0]][top.coordinate[1]] == 'e') {
                    return result;
                }
                for (int[] d : directions) {
                    int x = top.coordinate[0] + d[0], y = top.coordinate[1] + d[1];
                    if (x >= 0 && x < row && y >= 0 && y <= col) {
                        if (maze[x][y] == 'X' && top.breakings > 0) {
                            queue.offer(new Step(new int[]{x, y}, top.breakings - 1));
                        } else {
                            queue.offer(new Step(new int[]{x, y}, top.breakings));
                        }
                    }
                }
            }
            result += 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        ShortestPathWithBreakings a = new ShortestPathWithBreakings();
        char[][] input = {
                {'O', 'O', 'O', 'O', 'O'},
                {'O', 'O', 'X', 'O', 'O'},
                {'O', 'X', 'X', 'O', 'X'},
                {'s', 'X', 'X', 'X', 'e'},
        };
        char[][] input2 = {
                {'O', 'O', 'O', 'O', 'O'},
                {'O', 'O', 'X', 'O', 'O'},
                {'O', 'X', 'X', 'O', 'X'},
                {'s', 'X', 'O', 'O', 'e'},
        };
        System.out.println(a.shortestPathWithOneBreaking(input, new int[]{3, 0}, new int[]{3, 4}));
        System.out.println(a.shortestPathWithOneBreaking(input2, new int[]{3, 0}, new int[]{3, 4}));
    }
}
