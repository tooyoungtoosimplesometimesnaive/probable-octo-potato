import org.junit.Assert;
import org.junit.Test;

public class BitBoardTest {
    @Test
    public void test0() {
        BitBoard board = BitBoard.allZeros(5, 5);
        board.set(2, 3, 1);
        Assert.assertEquals(board.toString(),
            "00000\n"
                + "00000\n"
                + "00010\n"
                + "00000\n"
                + "00000\n");

        board.set(2, 3, 0);
        Assert.assertEquals(board.toString(),
            "00000\n"
                + "00000\n"
                + "00000\n"
                + "00000\n"
                + "00000\n");

        board.set(4, 3, 1);
        Assert.assertEquals(board.toString(),
            "00000\n"
                + "00000\n"
                + "00000\n"
                + "00000\n"
                + "00010\n");
    }
    @Test
    public void test1() {
        BitBoard board1 = BitBoard.allOnes(5, 5);
        board1.set(2, 3, 0);
        Assert.assertEquals(board1.toString(),
            "11111\n"
                + "11111\n"
                + "11101\n"
                + "11111\n"
                + "11111\n");
        board1.set(2, 4, 0);
        Assert.assertEquals(board1.toString(),
            "11111\n"
                + "11111\n"
                + "11100\n"
                + "11111\n"
                + "11111\n");
        board1.set(0, 4, 0);
        Assert.assertEquals(board1.toString(),
            "11110\n"
                + "11111\n"
                + "11100\n"
                + "11111\n"
                + "11111\n");
        board1.set(4, 0, 0);
        Assert.assertEquals(board1.toString(),
            "11110\n"
                + "11111\n"
                + "11100\n"
                + "11111\n"
                + "01111\n");
    }

    @Test
    public void testConversion() {
        BitBoard ones = BitBoard.allOnes(5, 6);
        for (int i = 0; i < 5; i ++) {
            for (int j = 0; j < 6; j++) {
                ones.set(i, j, 0);
            }
        }
        Assert.assertEquals(ones.toString(), BitBoard.allZeros(5, 6).toString());

        BitBoard zeros = BitBoard.allZeros(5, 6);
        for (int i = 0; i < 5; i ++) {
            for (int j = 0; j < 6; j++) {
                zeros.set(i, j, 1);
            }
        }
        Assert.assertEquals(zeros.toString(), BitBoard.allOnes(5, 6).toString());
    }
}
