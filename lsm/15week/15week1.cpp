#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    // ���� ������ �Ÿ��� mid, mid���� ������ ������ ���� �����ϴ� ����
    // start�� 1, end�� distance, mid�� �� ���� ���
    // �� ���� ������ cnt, �񱳴�� ���� ������ ��ġ�� prev
    // rocks�� �����ϰ� �տ������� ������ ����
    // rocks = [2,14,11,21,17] -> [2,11,14,17,21],25
    // mid�� (1+25)/2 = 13�̶�� 2-0(0��° �� ����), 11-0(1��° �� ����), 14-0 17-14(3��° �� ����), 21-14(4��° �� ����), 25-14(������ ���� �� 1�� ����) -> �� 5�� ����
    // n�� 2�ε� 5���� �����ؼ� end=mid-1�� �ؼ� �ٽ� �ݺ�, ���� n������ ���� ���� �����ߴٸ� start=mid+1�� �ؼ� �˰��� �ݺ�. n���� ���� ���� �����ߴٸ� �Ÿ��� �ּڰ� �� ���� ū ���� ���ؾ� �ؼ� start=mid+1
    int answer = 0;
    int start = 1, mid, end = distance;
    int cnt, prev;

    sort(rocks.begin(), rocks.end()); // ����

    while (start <= end) { // start�� end���� Ŀ�� ������ while�� �ݺ�
        mid = (start + end) / 2;
        cnt = 0;
        prev = 0;

        for (int i = 0; i < rocks.size(); ++i) { // ����������� ���� ���� ���� Ȯ��
            if (mid > rocks[i] - prev)
                ++cnt;
            else
                prev = rocks[i];
        }

        if (mid > distance - prev) // �߰��� ������ ���� �������� ��
            ++cnt;

        if (cnt > n) // ���� �� ���� �����ߴٸ�
            end = mid - 1;
        else { // ���� ���ų� �� �����ߴٸ�
            start = mid + 1;
            answer = mid;
        }
    }
    return answer;
}
