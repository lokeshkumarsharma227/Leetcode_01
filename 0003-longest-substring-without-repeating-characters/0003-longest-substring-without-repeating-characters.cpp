class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength=0;
        int l=0;
        int i=0;
        unordered_set<char>set;
        for(i=0;i<s.length();i++){
            while(set.find(s[i])!=set.end()){
                set.erase(s[l]);
                l++;
            }
            set.insert(s[i]);
            maxLength=max(maxLength,i-l+1);
        }
        return maxLength;
        
    }
};