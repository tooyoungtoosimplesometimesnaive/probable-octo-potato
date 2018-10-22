import org.junit.Test;

public class BitBoardTest {
    @Test
    public void test() {
        BitBoard board = BitBoard.allZeros(5, 5);
        board.set(2, 3, 1);
        board.printBoard();
        BitBoard board1 = BitBoard.allOnes(5, 5);
        board1.printBoard();
        board1.set(2, 3, 0);
    }
}
