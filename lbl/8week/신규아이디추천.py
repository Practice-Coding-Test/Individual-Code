def solution(new_id):
    new_id = new_id.lower()
    new2 = ''
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in ['-','_','.']:
            new2 += new_id[i]
    new3 = ''
    for i in range(len(new2)):
        if new3 and new3[-1] == '.' and new2[i] == '.':
            continue
        else:
            new3 += new2[i]
    if new3 and new3[0] == '.':
        new3 = new3[1:]
    if new3 and new3[-1] == '.':
        new3 = new3[:-1]
    if not new3:
        new3 = 'a'
    if len(new3) >= 16:
        new3 = new3[:15]
    if new3 and new3[-1] == '.':
        new3 = new3[:-1]
    while len(new3) <= 2:
        new3 += new3[-1]
    return new3
