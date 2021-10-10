import java.util.ArrayList;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int minRank = 7; int maxRank = 0; int zero = 0;
        ArrayList<Integer> win_numsArr = new ArrayList<>(win_nums.length);

        for (int w : win_nums) {
            win_numsArr.add(w);
        }
        
        for(int l : lottos) {
            if(l == 0) {
                zero++;
            } else if(win_numsArr.contains(l)){
                minRank--;
            }
        }
    
        minRank = (minRank == 7) ? 6 : minRank;
        maxRank = (zero == 6) ? 1 :  minRank - zero;
        int[] answer = {maxRank, minRank};
        
        return answer;
    }
}
