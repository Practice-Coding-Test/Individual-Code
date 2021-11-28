#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> h; // define priority queue

    // heap enqueue
    for (int i = 0; i < scoville.size(); i++) {
        h.push(scoville[i]);
    }

    // sum mean1, mean2
    while (h.size() > 1 && h.top() < K) {
        int mean1 = h.top();
        h.pop();
        int mean2 = h.top();
        h.pop();
        int scoville_new = mean1 + (mean2 * 2);
        h.push(scoville_new);
        answer++;

    }
    // heap dequeue
    while (!h.empty()) {
        if (h.top() < K) {
            return -1;
        }
        h.pop();
    }
    return answer;

}