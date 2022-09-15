
from collections import deque
 
def solution(n, t, m, timetable):
    answer = 0
    answer_str = ''
    time = deque()
    for ti in timetable:
        hour, minute = ti.split(":")
        hour = int(hour) * 60
        minute = int(minute)
        time.append(hour + minute)
    time = deque(sorted(time))
    bus_time = 540
    for _ in range(n):
        max_cnt = m
        last = bus_time
        while time:
            if max_cnt != 0 and time[0] <= bus_time:
                last = time.popleft()
                max_cnt -= 1
            else:
                break
        if _ == n - 1 and max_cnt == 0:
            answer = last - 1
        elif _ == n - 1 and max_cnt != 0:
            answer = bus_time
        bus_time += t
    ah = str(answer // 60)
    am = str(answer % 60)
    if len(ah) == 1:
        ah = '0' + ah
    if len(am) == 1:
        am = '0' + am
    answer_str = ah + ":" + am
    return answer_str
