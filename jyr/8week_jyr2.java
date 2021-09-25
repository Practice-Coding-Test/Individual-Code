class Solution {
    public static int getMove(int n) {
        switch(n){
            case 1, 3:
                return 1;
            case 2, 4, 6:
                return 2;
            case 5, 7, 9:
                return 3;
            case 8, 10:
                return 4;
            default:
                return 0;
        }
    }

    public static String getCloseHand(int distL, int distR) {
        int moveL = getMove(Math.abs(distL));
        int moveR = getMove(Math.abs(distR));

        if(moveL > moveR) {
            return "R";
        } else if( moveL < moveR) {
            return "L";
        } else {
            return "equal";
        }
    }

    public static String solution(int[] numbers, String hand) {
        String answer = "";
        int l = 10; int r = 12; int distL = 0; int distR = 0;
        String closeHand = "";

        for(int n : numbers) {
            // 왼손
            if(n % 3 == 1) {
                l = n;
                answer += "L";
            }
            // 거리 계산 
            else if(n % 3 == 2 || n == 0) {
                closeHand = (n == 0)? getCloseHand(11 - l, 11 -r) : getCloseHand(n - l, n - r);

                answer = (closeHand.equals("equal")) ? answer + hand.substring(0,1).toUpperCase() : answer + closeHand;

                if(answer.substring(answer.length() - 1).equals("L")) {
                    l = (n == 0)? 11 : n;
                } else {
                    r = (n == 0)? 11 : n;
                }

            } else {
                r = n;
                answer += "R";
            }
        }
        return answer;
    }
}