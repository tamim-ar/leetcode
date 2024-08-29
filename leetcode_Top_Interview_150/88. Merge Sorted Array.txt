class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int a1 = m - 1;
        int a2 = n - 1;
        int i = m + n - 1;

        while (a2 >= 0) {
            if (a1 >= 0 && nums1[a1] > nums2[a2]) {
                nums1[i--] = nums1[a1--];
            } else {
                nums1[i--] = nums2[a2--];
            }
        }
    }
}