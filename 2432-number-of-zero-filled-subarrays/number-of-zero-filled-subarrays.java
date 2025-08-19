class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long cnt = 0L;
        long local = 0L;
        for (int n : nums) {
            if (n == 0) {
                cnt += ++local;
            } else {
                local = 0;
            }
        }
        return cnt;
    }
}