import com.sun.tools.javac.util.Assert;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

public class ShortestPathWithBreakings {
    static class Step {
        int[] coordinate;
        int breakings;
        Step(int[] coordinate, int breakings) {
            this.coordinate = coordinate;
            this.breakings = breakings;
        }
        @Override
        public String toString() {
            return "[" + coordinate[0] + "," + coordinate[1] + "]," + breakings;
        }
    }

    private int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int shortestPathWithOneBreaking(char[][] maze, int[] start, int[] end) {
        int row = maze.length;
        int col = maze[0].length;
        Deque<Step> queue = new ArrayDeque<>();
        queue.offer(new Step(start, 1));

        Set<String> visited = new HashSet<>();
        int result = 0;
        while (!queue.isEmpty()) {
            int s = queue.size();
            for (int i = 0; i < s; i++) {
                Step top = queue.poll();
//                System.out.println(top.coordinate[0] + ", " + top.coordinate[1] + ", break=" + top.breakings +", path=" + result);
                if (top.coordinate[0] == end[0] && top.coordinate[1] == end[1]) {
                    return result;
                }

                visited.add(top.toString());

                for (int[] d : directions) {
                    int x = top.coordinate[0] + d[0], y = top.coordinate[1] + d[1];
                    if (x >= 0 && x < row && y >= 0 && y < col) {
                        if (x == start[0] && y == start[1]) {
                            continue;
                        }
                        if (maze[x][y] == 'X' && top.breakings > 0) {
                            Step nextStep = new Step(new int[]{x, y}, top.breakings - 1);
                            if (!visited.contains(nextStep.toString())) {
                                queue.offer(nextStep);
                            }
                        } else if (maze[x][y] == 'O' || maze[x][y] == 'e') {
                            Step nextStep = new Step(new int[]{x, y}, top.breakings);
                            if (!visited.contains(nextStep.toString())) {
                                queue.offer(nextStep);
                            }
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
        char[][] input3 = {
                {'O', 'O', 'O', 'O', 'O'},
                {'O', 'O', 'X', 'O', 'X'},
                {'O', 'X', 'X', 'X', 'X'},
                {'s', 'X', 'O', 'X', 'e'},
        };
        Assert.check(a.shortestPathWithOneBreaking(input, new int[]{3, 0}, new int[]{3, 4}) == 10);
        Assert.check(a.shortestPathWithOneBreaking(input2, new int[]{3, 0}, new int[]{3, 4}) == 4);
        Assert.check(a.shortestPathWithOneBreaking(input3, new int[]{3, 0}, new int[]{3, 4}) == -1);
    }
}
