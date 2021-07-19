#include <vector>
#include <iostream>

int maxCount(int m, int n, std::vector<std::vector<int>>& ops) {
    for (size_t index = 0; index < ops.size(); index++)
    {
        if(m > ops[index][0]) m = ops[index][0];
        if(m > ops[index][1]) n = ops[index][0];
    }
    return m * n;
}

int main(int argc, char const *argv[])
{
    std::vector<std::vector<int>> ops = {{2,2},{3,3},{3,3},{3,3},{2,2},{3,3},{3,3},{3,3},{2,2},{3,3},{3,3},{3,3}};
    std::printf("%d\n", maxCount(3, 3, ops));
    return 0;
}
