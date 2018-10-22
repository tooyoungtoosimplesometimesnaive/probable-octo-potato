/**
 * A board with zeroes and ones.
 * Storing every row as an integer.
 */
public class BitBoard {
    private int[] board;
    private int row;
    private int col;
    public BitBoard(int row, int col) {
        this.row = row;
        this.col = col;
        this.board = new int[row];
    }

    static BitBoard allOnes(int row, int col) {
        int rowNum = (1 << (col + 1)) - 1;
        BitBoard b = new BitBoard(row, col);
        for (int i = 0; i < row; i++) {
            b.setRowNumber(i, rowNum);
        }
        return b;
    }

    static BitBoard allZeros(int row, int col) {
        return new BitBoard(row, col);
    }

    // Some problems here
    public void set(int i, int j, int value) {
        if (value != 0 && value != 1) {
            throw new IllegalArgumentException("Value should be either 0 or 1");
        }
        int n = get(i, j);
        if (n == value) {
            return;
        } else {
            // 0 ^ 1 -> 1
            // 1 ^ 1 -> 0
            int rowNum = board[i];
            int remaining = rowNum & ((1 << j + 1) - 1);
            board[i] = ((rowNum - remaining) ^ 1) + remaining;
        }
    }

    public int get(int i, int j) {
        int rowNum = board[i];
        return (rowNum & (1 << j)) == 0 ? 0 : 1;
    }

    public void setRowNumber(int i, int rowNumber) {
        board[i] = rowNumber;
    }
    public void printBoard() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(get(i, j) + " ");
            }
            System.out.println();
        }
    }
}
