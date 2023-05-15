// Silver 5. How much is your Average

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string sub;
    float score;
    string record;

    double sum = 0;
    double cnt = 0;

    for (int i = 0; i < 20; i++)
    {
        cin >> sub >> score >> record;

        double grade = 0;
        switch (record[0])
        {
            case 'A': 
                grade = 4;
                break;
            case 'B':
                grade = 3;
                break;
            case 'C':
                grade = 2;
                break;
            case 'D':
                grade = 1;
                break;
            case 'F':
                grade = 0;
                break;
            case 'P':
                grade = 0;
                score = 0;
        }

        if (record[1] == '+')
        {
            grade += 0.5;
        }

        sum += grade * score;
        cnt += score;
    }

    cout << sum / cnt;
}