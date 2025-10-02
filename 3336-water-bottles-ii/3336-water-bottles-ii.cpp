class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int res = numBottles, empty = numBottles;
        numBottles = 0;
        while (numBottles > 0 || empty >= numExchange) {
            empty -= numExchange;
            numBottles++;
            numExchange++;
            if (numBottles > 0) {
                res++;
                numBottles--;
                empty++;
            }
        }
        return res;
    }
};