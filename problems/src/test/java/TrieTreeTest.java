import common.TrieTree;
import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class TrieTreeTest {
    @Test
    public void ttt() {
        TrieTree trieTree = new TrieTree(Arrays.asList("abcd", "abce", "ab", "abc", "aaaa", "aae"));
//        TrieTree trieTree = new TrieTree(Arrays.asList("abcd"));
        Assert.assertTrue(trieTree.search("ab"));
        Assert.assertTrue(trieTree.search("abcd"));
        Assert.assertEquals(trieTree.searchPrefix("ab").toString(), "[ab, abc, abcd, abce]");
    }
}
