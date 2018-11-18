package pq;

import java.util.PriorityQueue;

public class CanoePaddle {
    static class Pair implements Comparable<Pair> {
        int i;
        int j;
        int height;
        public Pair(int i, int j, int height) {
            this.i = i;
            this.j = j;
            this.height = height;
        }
        @Override
        public int compareTo(Pair other) {
            if (other.height == this.height) return 0;
            else return other.height > this.height ? -1 : 1;
        }
    }

    private int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int minDays(int[][] heightMap) {
        if (heightMap == null) {
            return 0;
        }

        int row = heightMap.length;
        if (row == 0) {
            return 0;
        }
        int col = heightMap[0].length;

        boolean[][] visited = new boolean[row][col];
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.offer(new Pair(0, 0, heightMap[0][0]));

        while (!pq.isEmpty()) {
            Pair head = pq.poll();
            if (head.i == row - 1 && head.j == col - 1) {
                return head.height;
            }
            for (int[] d : directions) {
                int x = head.i + d[0];
                int y = head.j + d[1];
                if (x >= 0 && x < row && y >= 0 && y < col && !visited[x][y]) {
                    visited[x][y] = true;
                    int currCost = Math.max(head.height, heightMap[x][y]);
                    pq.offer(new Pair(x, y, currCost));
                }
            }
        }

        // Will never reach this line.
        return -1;
    }

}
