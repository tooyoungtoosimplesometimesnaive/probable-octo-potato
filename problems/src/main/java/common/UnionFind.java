package common;

public class UnionFind {
  private int[] ids;
  private int[] sizes;
  public UnionFind(int size) {
    sizes = new int[size];
    ids = new int[size];
    for (int i = 0; i < size; i++) {
      ids[i] = i;
      sizes[i] = 1;
    }
  }

  public int root(int i) {
    int root = i;
    while (root != ids[root]) {
      root = ids[root];
    }

    // Path compression:
    while (i != root) {
      int tmp = ids[i];
      ids[i] = root;
      i = tmp;
    }
    return root;
  }

  public boolean find(int a, int b) {
    return root(a) == root(b);
  }

  public void union(int a, int b) {
    int rootA = root(a);
    int rootB = root(b);

    // Balancing the tree:
    if (sizes[rootA] > sizes[rootB]) {
      ids[rootB] = rootA;
      sizes[rootA] += sizes[rootB];
    } else {
      ids[rootA] = rootB;
      sizes[rootB] += sizes[rootA];
    }
  }
}
