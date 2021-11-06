import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub('[^\w.-]', '', new_id) # 2단계
    new_id = re.sub('\.{2,}', '.', new_id) # 3단계

    if new_id.startswith('.'): # 4단계
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    if len(new_id) == 0: # 5단계
        new_id = 'a'

    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]

    if len(new_id) <=2: # 7단계
        while len(new_id)!=3:
            new_id = new_id + new_id[-1]

    return new_id
