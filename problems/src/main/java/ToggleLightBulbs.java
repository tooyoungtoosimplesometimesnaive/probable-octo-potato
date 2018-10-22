import java.util.ArrayList;
import java.util.List;

public class ToggleLightBulbs {
    private int[][] board;
    private int size;
    private int total;
    public ToggleLightBulbs(int size) {
        this.size = size;
        this.total = size * size;
        this.board = new int[size][size];
        System.out.println(this.board);
    }

    public void solve() {
        solve(0, new ArrayList<>());
    }

    private void solve(int i, List<Integer> path) {
        if (i >= total) {
            if (check()) {
                System.out.println("Got it");
                printSolutionPath(path);
            }
            return;
        }
        int x = i / size;
        int y = i % size;
        toggle(x, y);
        path.add(i);
        solve(i + 1, path);
        toggle(x, y);
        path.remove(path.size() - 1);
        solve(i + 1, path);
    }

    private void toggle(int x, int y) {
       int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
       for (int[] d : directions) {
           int dx = d[0];
           int dy = d[1];

           if (x + dx >= 0 && x + dx < size && y + dy >= 0 && y + dy < size) {
               board[x + dx][y + dy] = board[x + dx][y + dy] == 1 ? 0 : 1;
           }
       }
    }

    private boolean check() {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (board[i][j] != 1) {
                    return false;
                }
            }
        }
        return true;
    }

    private void printSolutionPath(List<Integer> path) {
        for (Integer i : path) {
            System.out.print("(" + i / size + "," + i % size + ") ");
        }
        System.out.println();
    }

    private void printBoard() {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
}
