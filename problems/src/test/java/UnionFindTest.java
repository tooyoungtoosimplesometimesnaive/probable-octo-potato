import common.UnionFind;
import org.junit.Assert;
import org.junit.Test;

public class UnionFindTest {
  @Test
  public void unionFindTest() {
    UnionFind uf = new UnionFind(10);

    uf.union(1, 2);
    uf.union(2, 3);
    uf.union(9, 8);
    uf.union(0, 3);

    Assert.assertTrue(uf.find(1, 3));
    Assert.assertFalse(uf.find(1, 9));

    Assert.assertEquals(uf.root(0), uf.root(3));

  }

}
