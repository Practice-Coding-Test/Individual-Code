#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days; // 각 기능이 몇 일 걸리는지 받는 vector
    cout << (progresses.size() != 0) << endl;
    cout << progresses.front() << endl;
    for (int i = 0; i < progresses.size(); i++) {
        float day = (float(100 - progresses[i])) / speeds[i]; // 100-93 / 1 -> 7일, 100-30 / 30 -> 2.xxx -> 3 (반올림)
        days.push_back(ceil(day));
    }

    int max_day = days[0]; // 첫 번째 day를 max_day로
    answer.push_back(1); // answer에 첫 번째 기능 개수인 1추가
    for (int i = 1; i < days.size(); i++)
    {
        if (max_day >= days[i]) { // 7일 > 3일
            answer[answer.size() - 1] += 1; // answer의 크기-1에 +=1 추가 (day[i]가 같이 배포되니까)
        }
        else { // 7일 < 9일
            max_day = days[i]; // 9일을 max_day로
            answer.push_back(1); // answer에 새로운 배포날짜 추가 (9일이 7일보다 커서, 얘를 기준으로 배포날짜가 새로 잡힘)
        }


    }
    return answer;
}