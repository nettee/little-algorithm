class Solution {
    public void rotate(int[] nums, int k) {
        int N = nums.length;
        k %= N;
        reverse(nums, 0, N);
        reverse(nums, 0, k);
        reverse(nums, k, N);
    }

    void reverse(int[] nums, int begin, int end) {
        for (int i = begin, j = end - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}