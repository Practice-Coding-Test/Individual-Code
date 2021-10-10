import java.util.*;

class Solution {
    public String[] solution(String[] record) {       
        List<String> answer = new ArrayList<>();
        String[][] inOuts = new String[record.length][2];
        HashMap<String, String> userInfo = new HashMap<>();
        
        for(int i = 0; i < record.length; i++){
            String inOut = record[i].split(" ")[0];
            String uid = record[i].split(" ")[1];
            
            if(inOut.equals("Leave") ) {
                inOuts[i][0] = inOut;
                inOuts[i][1] = uid;
                continue;
            } 
            
            String nickname = record[i].split(" ")[2];
            if(inOut.equals("Change")) {
                userInfo.replace(uid, nickname);
            } else {
                userInfo.put(uid,nickname);
                inOuts[i][0] = inOut;
                inOuts[i][1] = uid;
            }
        }
        
        for(int i = 0; i < inOuts.length; i++) {
            if(inOuts[i][0] == null)  continue; 
            
            String enterOrLeave = inOuts[i][0].equals("Enter")? "님이 들어왔습니다." : "님이 나갔습니다.";
            String _nickname = userInfo.get(inOuts[i][1]);
            answer.add(_nickname + enterOrLeave);   
        }       
 
        return answer.toArray(new String[0]);
    }
}
