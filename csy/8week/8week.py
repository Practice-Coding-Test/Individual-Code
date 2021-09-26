def solution(record):
    answer = []
    user = {} # 닉네임 (딕셔너리)
    actions = [] # "Enter", "Leave", "Change"
    
    for event in record :
        action = event.split(" ")[0]
        userID = event.split(" ")[1]
        
        if action in ("Enter", "Change") : # 닉네임 변경 발생 가능
                                           # 새로운 사용자면 추가되고, 기존 사용자면 닉네임 변경
            nickname = event.split(" ")[2]
            user[userID] = nickname
        actions.append((action, userID))
            
    for enter in actions :
        action = enter[0]
        userID = enter[1]
        if action == "Enter" :
            answer.append(user[userID] + "님이 들어왔습니다.")
        elif action == "Leave" :
            answer.append(user[userID] + "님이 나갔습니다.")
            
    return answer
