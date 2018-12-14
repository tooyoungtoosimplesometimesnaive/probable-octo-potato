class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int row = matrix.length;
        if (row == 0) {
            return 0;
        }
        int col = matrix[0].length;
        
        int[][] prefixMatrix = new int[row + 1][col];
        
        for (int j = 0; j < col; j ++) {
            for (int i = 1; i < row + 1; i++) {
                prefixMatrix[i][j] = prefixMatrix[i - 1][j] + matrix[i - 1][j];
            }
        }
        
        for (int i = 0; i < row + 1; i ++) {
            for (int j = 0; j < col; j ++) {
                System.out.print(prefixMatrix[i][j] + " ");
            }
            System.out.println();
        }
        int result = Integer.MIN_VALUE;
        for (int i = 0; i < row; i++) {
            for (int j = i; j < row; j++) {
                TreeSet<Integer> treeSet = new TreeSet<>();
                int sum = 0;
                treeSet.add(sum);
                for (int h = 0; h < col; h++) {
                    int s = prefixMatrix[j + 1][h] - prefixMatrix[i][h];
                    sum += s;
                    Integer c = treeSet.ceiling(sum - k);
                    if (c != null) {
                        result = Math.max(result, (sum - c));
                    }
                    treeSet.add(sum);
                }
                
            }
        }
        return result;
    }
}
