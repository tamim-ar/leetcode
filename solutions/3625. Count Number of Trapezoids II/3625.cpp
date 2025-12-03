class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<float,vector<float>> slope_intercept;
        unordered_map<int, vector<float>> midp_slope;
        for(int i=0;i<n;i++){
            int x1 = points[i][0], y1 = points[i][1];
            for(int j=i+1;j<n;j++){
                int x2 = points[j][0], y2 = points[j][1];
                int dy = y2 - y1, dx = x2 - x1;
                float slope,intercept;
                if(dx==0){
                    slope = 1e9 + 7;
                    intercept = x1;
                }else{
                    slope = (float)(dy)/(dx);
                    intercept = (float)(y1*dx - x1*dy)/(dx);
                }
                slope_intercept[slope].push_back(intercept);
                int midp = (x1 + x2)*10000 + (y1+y2);
                midp_slope[midp].push_back(slope);
            }
        }
        int ans = 0;
        for(auto &[slope, v_of_intercept] : slope_intercept){
            if(v_of_intercept.size()==0) continue;
            unordered_map<float,int> cnt;
            for(float intercept : v_of_intercept){
                cnt[intercept]++;
            }
            long long sum = 0, sum_of_sq = 0;
            for(auto &[k,v] : cnt){
                sum += v;
                sum_of_sq += (long long)v*v;
            }
            long long result = ((long long)sum*sum - sum_of_sq)/2;
            ans += result;
        }
        // subtracting parallelograms :
        for(auto &[midp, v_of_slope] : midp_slope){
            if(v_of_slope.size()==0) continue;
            unordered_map<float,int> cnt;
            for(float slope : v_of_slope){
                cnt[slope]++;
            }
            long long sum = 0, sum_of_sq = 0;
            for(auto &[k,v] : cnt){
                sum += v;
                sum_of_sq += (long long)v*v;
            }
            long long result = ((long long)sum*sum - sum_of_sq)/2;
            ans -= result;
        }
        return ans;
    }
};