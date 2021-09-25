class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] wear = new int[n];
        int answer = 0;

        for (int i : reserve) {
            wear[i - 1]++;
        }

        for (int i : lost) {
            wear[i - 1]--;
        }

        for (int i = 0; i < n; i++) {
            if (wear[i] == -1) {
                if (i != 0 && wear[i - 1] == 1) {
                    wear[i]++;
                    wear[i - 1]--;
                } else if (i != n - 1 && wear[i + 1] == 1) {
                    wear[i]++;
                    wear[i + 1]--;
                }
            }
        }

        for (int i : wear) {
            if (i == -1) {
                continue;
            }
            answer++;
        }
        return answer;
    }
}
