#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days; // �� ����� �� �� �ɸ����� �޴� vector
    cout << (progresses.size() != 0) << endl;
    cout << progresses.front() << endl;
    for (int i = 0; i < progresses.size(); i++) {
        float day = (float(100 - progresses[i])) / speeds[i]; // 100-93 / 1 -> 7��, 100-30 / 30 -> 2.xxx -> 3 (�ݿø�)
        days.push_back(ceil(day));
    }

    int max_day = days[0]; // ù ��° day�� max_day��
    answer.push_back(1); // answer�� ù ��° ��� ������ 1�߰�
    for (int i = 1; i < days.size(); i++)
    {
        if (max_day >= days[i]) { // 7�� > 3��
            answer[answer.size() - 1] += 1; // answer�� ũ��-1�� +=1 �߰� (day[i]�� ���� �����Ǵϱ�)
        }
        else { // 7�� < 9��
            max_day = days[i]; // 9���� max_day��
            answer.push_back(1); // answer�� ���ο� ������¥ �߰� (9���� 7�Ϻ��� Ŀ��, �긦 �������� ������¥�� ���� ����)
        }


    }
    return answer;
}