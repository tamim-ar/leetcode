#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        unordered_map<int,int> freq;
        int evenD = 0, oddD = 0;
        int l = 0, ans = 0;

        for (int r = 0; r < (int)nums.size(); r++) {
            int x = nums[r];
            int &fx = freq[x];
            fx++;
            if (fx == 1) {
                if (x % 2 == 0) evenD++;
                else oddD++;
            }

            while (l <= r && (evenD > oddD || oddD > evenD)) {
                int y = nums[l++];
                int &fy = freq[y];
                fy--;
                if (fy == 0) {
                    if (y % 2 == 0) evenD--;
                    else oddD--;
                    freq.erase(y);
                }
            }

            if (evenD == oddD) ans = max(ans, r - l + 1);
        }

        return ans;
    }
};
