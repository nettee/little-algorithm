class Solution {
    public int maxTurbulenceSize(int[] A) {
        if (A.length <= 1) {
            return A.length;
        }

        int N = A.length;
        // 定义两个 DP 数组 f, g
        int[] f = new int[N+1];
        int[] g = new int[N+1];
        f[0] = 0;
        g[0] = 0;
        f[1] = 1;
        g[1] = 1;

        int res = 1;
        for (int k = 2; k <= N; k++) {
            if (A[k-2] < A[k-1]) {
                f[k] = g[k-1] + 1;
                g[k] = 1;
            } else if (A[k-2] > A[k-1]) {
                f[k] = 1;
                g[k] = f[k-1] + 1;
            } else {
                f[k] = 1;
                g[k] = 1;
            }
            res = Math.max(res, f[k]);
            res = Math.max(res, g[k]);
        }
        return res;
    }
}