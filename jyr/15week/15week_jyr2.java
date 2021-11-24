// 특정 문자 뒤집기(toCharArray())

import java.util.*;

class Main {
	public ArrayList<String> solution(int n, String[] str){
		String answer;
		char[] s = str.toCharArray();
		int lt=0, rt=str.length()-1;
		while(lt<rt){
			if(!Character.isAlphabetic(s[lt]) lt++;
			else if(!Character.isAlphabetic(s[rt]) rt--;
			else{
				car tmp=s[lt];
				s[lt]=s[rt];
				s[rt]=tmp;
				lt++;
				rt--;
			}
		}
		answer = String.valueOf(s);
		return answer;
	}

	public static void main(String[] args){
		Main T = new Main();
		Scanner sc = new Scanner(System.in);
		String n = sc.next();
		System.out.println(T.solution(str));
	}
}
