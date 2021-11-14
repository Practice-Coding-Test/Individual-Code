import java.util.Scanner;

// solution 함수에 static 쓰면 객체 생성 필요 X
public class Main {
    public int solution(String str, char t){
        int answer = 0;
        str = str.toUpperCase();
        t = Character.toUpperCase(t);

//        for(int i = 0; i < str.length(); i++){
//            if(str.charAt(i) == t) answer++;
//        }

        for(char x : str.toCharArray()) { // string은 for each 문에 올 수 없음
            if(x == t) answer++;
        }

        return answer;
    }

    public static void main(String[] args){
        Main T = new Main(); // static이면 이거 필요 없어
        Scanner sc = new Scanner(System.in);
        String str = sc.next(); // 여기까진 문장
        char c = sc.next().charAt(0);

        System.out.println(T.solution(str, c));
    }
}
