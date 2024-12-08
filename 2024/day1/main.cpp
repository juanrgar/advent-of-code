
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

static void print_vec(const std::vector<long> & v)
{
    for (auto&& e : v) {
        std::cout << e << std::endl;
    }
}


int main(int argc, char *argv[])
{
    std::ifstream input1("input1.txt");

    std::vector<long> l_col;
    std::vector<long> r_col;

    std::string line;

    while (std::getline(input1, line)) {
        std::stringstream ss(line);

        unsigned num;
        ss >> num;
        l_col.push_back(num);
        ss >> num;
        r_col.push_back(num);
    }

    input1.close();

    std::sort(l_col.begin(), l_col.end());
    std::sort(r_col.begin(), r_col.end());

    std::vector<unsigned> subs(l_col.size());

    for (size_t i = 0; i < l_col.size(); ++i) {
        subs[i] = std::abs(l_col[i] - r_col[i]);
    }

    unsigned res = std::accumulate(subs.begin(), subs.end(), 0);

    std::cout << res << std::endl;


    unsigned long score = 0;

    for (auto && e : l_col) {
        unsigned long count = std::count(r_col.begin(), r_col.end(), e);

        score += count * e;
    }

    std::cout << score << std::endl;

    return 0;
}
