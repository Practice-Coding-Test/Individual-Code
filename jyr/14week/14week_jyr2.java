import java.util.*;

/*  방법 1.
 *  char 대/소문자 판별  Character.isLowerCase(x);
 *  char 대/소문자 변경  Character.toLowerCase(x);
 *  방법 2.
 *  대문자 65 ~ 90
 *  소문자 97 ~ 122 .. 32 차이
 */
public class Main {
    public String solution(String str){
        String answer = "";

//        for(char x : str.toCharArray()) { // string은 for each 문에 올 수 없음
//            if(Character.isLowerCase(x)) answer += Character.toUpperCase(x);
//            else answer += Character.toLowerCase(x);
//        }

        for(char x : str.toCharArray()){
            if(x >= 97 && x <= 122) answer += (char)(x-32);
            else answer += (char)(x+32);
        }
        
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        System.out.println(T.solution(str));
    }
}
