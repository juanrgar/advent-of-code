
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

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

        unsigned char dir;
        ss >> dir;
        l_col.push_back(dir);

        unsigned long num;
        ss >> num;
        r_col.push_back(num);
    }

    input1.close();

//    {
//        long pos = 50;
//        unsigned count = 0;
//
//        for (auto i{0}; i < l_col.size(); i++) {
//            const unsigned char dir = l_col[i];
//            const unsigned long num = r_col[i];
//
//            long mov = num * ((dir == 'L') ? -1 : 1);
//
//            pos += mov;
//            pos %= 100;
//            if (pos < 0) pos = 100 + pos;
//            // https://www.learncpp.com/cpp-tutorial/remainder-and-exponentiation/
//
//            if (pos == 0) count++;
//        }
//
//        std::cout << count << std::endl;
//    }

    {
        // TODO
        long pos = 50;
        unsigned count = 0;

        for (auto i{0}; i < l_col.size(); i++) {
            const unsigned char dir = l_col[i];
            const unsigned long num = r_col[i];

            long mov = num * ((dir == 'L') ? -1 : 1);

            cout << "======" << endl;
            cout << "pos " << pos << endl;
            cout << "mov " << mov << endl;

            long diff = 0;
            if (mov > 0) {
                diff = 100 - pos;
            } else {
                diff = pos;
            }

            long abs_mov = abs(mov);
            unsigned full_spins = (abs_mov / 100);

            count += full_spins;

            abs_mov -= (full_spins * 100);
            if ((abs_mov > 0) && (pos != 0) && (abs_mov >= diff)) {
                count++;
            }

            cout << "count " << count << endl;

            pos += mov;
            pos %= 100;
            if (pos < 0) pos = 100 + pos;
            // https://www.learncpp.com/cpp-tutorial/remainder-and-exponentiation/
            cout << "pos " << pos << endl;
        }

        std::cout << count << std::endl;
    }

    return 0;
}
