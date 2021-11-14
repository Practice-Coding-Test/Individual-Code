import java.util.*;

public class Main {
    public String solution(String str){
        String answer = "";
        int maxLen = Integer.MIN_VALUE; // 최솟값
        String[] s = str.split(" "); // ' '는 char라 X
        for(String x : s){
            if(maxLen < x.length()) {
                maxLen = x.length();
                answer = x;
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine(); // 한 줄을 입력받을거니까 nextLine()

        System.out.println(T.solution(str));
    }
}
