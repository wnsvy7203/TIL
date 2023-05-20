#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    while(1)
    {
        int a, b, c;
        
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0)
        {
            break;
        }
        
        vector<int> nums(3);
        
        nums[0] = a;
        nums[1] = b;
        nums[2] = c;
        
        for (int i = 0; i < nums.size(); i++)
        {
            cout << nums[i];
        }

        sort(nums.begin(), nums.end());
        
        if (nums[0] + nums[1] > nums[2])
        {
            cout << "Invalid" << '\n';
        }
        else
        {
            if (nums[0] == nums[1] && nums[1] == nums[2])
            {
                cout << "Equilateral" << '\n';
            }
            else if (nums[0] == nums[1] || nums[1] == nums[2])
            {
                cout << "Isosceles" << '\n';
            }
            else
            {
                cout << "Scalene" << '\n';
            }
        }
    }
}