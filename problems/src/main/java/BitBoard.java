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
        int rowNum = (1 << col) - 1;
        BitBoard b = new BitBoard(row, col);
        for (int i = 0; i < row; i++) {
            b.setRowNumber(i, rowNum);
        }
        return b;
    }

    static BitBoard allZeros(int row, int col) {
        return new BitBoard(row, col);
    }

    public void set(int i, int j, int value) {
        if (value != 0 && value != 1) {
            throw new IllegalArgumentException("Value should be either 0 or 1");
        }
        checkIndexRange(i, j);

        j = col - 1 - j;
        int rowNum = board[i];
        int leading = rowNum & (~((1 << (j + 1)) - 1));
        // j ones
        // xxxxx
        // x1000
        // x0111
        int remaining = rowNum & ((1 << j) - 1);
        value = value << j;
        board[i] = leading + value + remaining;
    }

    public int get(int i, int j) {
        int rowNum = board[i];
        return (rowNum & (1 << j)) == 0 ? 0 : 1;
    }

    public void setRowNumber(int i, int rowNumber) {
        board[i] = rowNumber;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < row; i++) {
            for (int j = col - 1; j >= 0; j--) {
                sb.append(get(i, j));
            }
            sb.append('\n');
        }
        return sb.toString();
    }

    private void checkIndexRange(int i, int j) {
        if (i < 0 || i >= row) {
            throw new IndexOutOfBoundsException();
        }
        if (j < 0 || j >= col) {
            throw new IndexOutOfBoundsException();
        }
    }
}
