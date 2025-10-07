class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        vector<int>ans(n,-1);
        unordered_map<int,int>ump;
        set<int>index;

        for(int i=0; i<n; i++){
            if(rains[i] == 0) index.insert(i);
            else{
                if(ump.find(rains[i]) == ump.end()) ump[rains[i]] = i;
                else{
                    auto ind = index.upper_bound(ump[rains[i]]);
                    if(ind == index.end()) return {};
                    ans[*ind] = rains[i];
                    index.erase(ind);
                    ump[rains[i]] = i;
                }
            }
        }
        for(auto i:index) ans[i]=1;
        return ans;
    }
};