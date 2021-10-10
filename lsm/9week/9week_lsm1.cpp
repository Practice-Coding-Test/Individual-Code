#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    // n명이 모두 심사받을 수 있는 시간의 최솟값
    // 심사대 1, 심사 5분, 2명 -> 시간=10
    // 6명을 2개의 심사대에서 (7분, 10분) 심사를 할 경우 제일 빠른 경우는?
    // 30분동안 7분 심사대는 4명 + 10분 심사대 3명 = 7명 -> 7명 > 6명 30분은 매우 충분
    // 30분 -> 15분, 15분일 때는 7분 2명+ 10분1명 = 3명 - 3명 < 6명 15분은 불충분
    // 15 -> 22 -> 26 -> 28 이렇게 해결할 수 있는 사람 수를 기준으로 시간의 최솟값을 찾아가도록 생각해야됨(완전 탐색은 시간이 너무 오래걸리니 이분탐색으로)
    long long answer = 0;

    sort(times.begin(), times.end()); // 정렬
    long long min = 1; // 가장 적게 걸리는 시간
    long long max = (long long)(times[times.size() - 1]) * n; // 가장 많이 걸리는 시간 = 모든 사람이 max심사대로 갈경우

    while (min <= max) {
        long long mid = (min + max) / 2;
        long long count = 0; // 평균적으로 심사받는 모든 수

        for (int i = 0; i < times.size(); i++) {
            count += mid / (long long)times[i]; // 각 시간마다, 평균적으로 심사받는 수를 모두 더해줌
        }

        if (count < n) {
            min = mid + 1; // 최소값을 mid+1로 좁힘

        }
        else { // mid시간동안 처리할 수 있는 모든 사람이 n보다 작을 때
            answer = mid; // 답에 mid
            max = mid - 1; // 범위를 좁힘
        }




    }

    return answer;
    // n명의 줄
    // 입국심사대 심사관마다 심사 시간은 다 다름
    // 처음 심사대는 비어있음
    // 한 심사대는 동시에 한 명까지
    // 가장 앞에 서 있는 사람은 비어 있는 심사대로(더 빨리 끝나는 심사대로 = 시간 계산)
    // 걸리는 시간 최소로
    // times배열 = 각 심사관이 한 명을 심사하는 데 걸리는 시간
    // answer = 모든 사람이 심사를 받는데 걸리는 시간의 최솟값

}