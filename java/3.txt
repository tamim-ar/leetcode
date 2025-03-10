class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int res = 0;
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);

        for (int i = 0, j = 0; j < n; j++) {
            i = Math.max(i, charIndex[s.charAt(j)] + 1);
            res = Math.max(res, j - i + 1);
            charIndex[s.charAt(j)] = j;
        }
        return res;
    }
}