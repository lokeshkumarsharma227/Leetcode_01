class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
     int count[10] = {0};
        for (int d : digits) {
            count[d]++;
        }

        std::vector<int> result;

        for (int num = 100; num <= 999; num += 2) {
            int a = num / 100;
            int b = (num / 10) % 10;
            int c = num % 10;

            int temp[10] = {0};
            temp[a]++;
            temp[b]++;
            temp[c]++;

            bool ok = true;
            for (int i = 0; i < 10; ++i) {
                if (temp[i] > count[i]) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                result.push_back(num);
            }
        }

        return result;
    }
};
