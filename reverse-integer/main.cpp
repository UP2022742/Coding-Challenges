class Solution {
public:
    int reverse(int x) {
        int rev_num = 0;
        while (x != 0){
            int curr_digit = x % 10;
            if (rev_num > 214748364 || (rev_num == 214748364 && curr_digit > 7)) return 0;
            if (rev_num < -214748364 || (rev_num == -214748364 && curr_digit < -8)) return 0;
            rev_num = (rev_num * 10) + curr_digit;
            x = x / 10;
        }
        return rev_num;
    }
};