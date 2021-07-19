#include <vector>
#include <iostream>
#include <algorithm> 

template <class T> void printVec(std::vector<T> vec){
    for (auto i = vec.begin(); i != vec.end(); ++i)
        std::cout << *i << std::endl;
}

// Runtime: 216 ms, faster than 29.61% of C++ online submissions for Valid Triangle Number.
// Memory Usage: 13 MB, less than 19.36% of C++ online submissions for Valid Triangle Number.

// O notation O(n^2/3); loop in loop in loop

int triangleNumber(std::vector<int>& nums){

    // Set a counter to return.
    int count = 0;

    // Save vector size as it's used numerous times.
    std::size_t vectorSize = nums.size();
    if(vectorSize < 3){
        return 0;
    }

    // Sort the vector incrementing order.
    std::sort(nums.begin(), nums.end());
    
    for (int side_a_index = 0; side_a_index < vectorSize - 2; side_a_index++) {
        int side_b_index = side_a_index + 1; // Index pos one above I
        int side_c_index = side_a_index + 2; // Index pos two above I

        for (side_b_index; side_b_index < vectorSize - 1; side_b_index++) {
            if(nums.at(side_a_index) == 0) break;

            // If the first two sides are NOT bigger than the third, iterate
            // the vector until you reach the end. If it reaches the end, break.
            while (side_c_index < vectorSize && \
                nums.at(side_a_index) + nums.at(side_b_index) > nums.at(side_c_index)) 
                side_c_index++;
            
            count += side_c_index - side_b_index - 1;
        }
    }
    return count;
}

// e.g. {1,2,4,5,8,9}
// side_a_index = 1;
// side_b_index = 2;
// side_c_index = 3;

// side_a_index: 1-5
// side_b_index: 2-8

// a+b > c
// b+c > a
// a+c > b

int main(int argc, char const *argv[])
{
    std::vector<int> nums = {2,2,3,4};
    std::cout << triangleNumber(nums) << std::endl;;
    return 0;
}
