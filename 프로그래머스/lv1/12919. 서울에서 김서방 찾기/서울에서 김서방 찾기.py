def solution(seoul):
    for index, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 "+str(index)+"에 있다" 
            return answer