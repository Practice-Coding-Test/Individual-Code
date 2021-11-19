#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    // 바위 사이의 거리를 mid, mid보다 간격이 좁으면 돌을 제거하는 형식
    // start는 1, end는 distance, mid는 두 값의 평균
    // 돌 제거 개수는 cnt, 비교대상 돌과 시작점 위치는 prev
    // rocks를 정렬하고 앞에서부터 간격을 구함
    // rocks = [2,14,11,21,17] -> [2,11,14,17,21],25
    // mid는 (1+25)/2 = 13이라면 2-0(0번째 돌 제거), 11-0(1번째 돌 제거), 14-0 17-14(3번째 돌 제거), 21-14(4번째 돌 제거), 25-14(마지막 남은 돌 1개 제거) -> 총 5개 제거
    // n은 2인데 5개를 제거해서 end=mid-1로 해서 다시 반복, 만약 n값보다 적은 돌을 제거했다면 start=mid+1로 해서 알고리즘 반복. n값과 같은 돌을 제거했다면 거리의 최솟값 중 가장 큰 값을 구해야 해서 start=mid+1
    int answer = 0;
    int start = 1, mid, end = distance;
    int cnt, prev;

    sort(rocks.begin(), rocks.end()); // 정렬

    while (start <= end) { // start가 end보다 커질 때까지 while문 반복
        mid = (start + end) / 2;
        cnt = 0;
        prev = 0;

        for (int i = 0; i < rocks.size(); ++i) { // 출발지점부터 돌간 사이 간격 확인
            if (mid > rocks[i] - prev)
                ++cnt;
            else
                prev = rocks[i];
        }

        if (mid > distance - prev) // 추가로 마지막 돌과 도착지점 비교
            ++cnt;

        if (cnt > n) // 돌을 더 많이 제거했다면
            end = mid - 1;
        else { // 돌을 같거나 덜 제거했다면
            start = mid + 1;
            answer = mid;
        }
    }
    return answer;
}
