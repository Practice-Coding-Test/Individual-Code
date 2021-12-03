import datetime
def solution(a, b):
    w = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = w[datetime.date(2016,a,b).weekday()]
    return answer