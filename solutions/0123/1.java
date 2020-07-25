class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }

        int s1 = Integer.MIN_VALUE;
        int s2 = 0;
        int s3 = Integer.MIN_VALUE;
        int s4 = 0;
        for (int p : prices) {
            s4 = Math.max(s4, s3 + p);
            s3 = Math.max(s3, s2 - p);
            s2 = Math.max(s2, s1 + p);
            s1 = Math.max(s1, -p);
        }
        return Math.max(0, Math.max(s2, s4));
    }
}