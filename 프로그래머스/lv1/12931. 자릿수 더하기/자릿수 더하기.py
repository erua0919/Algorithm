def solution(n):
    answer = 0
    def sum_digit(number):
        if number < 10:
            return number;
        return (number % 10) + sum_digit(number // 10) 
    answer +=sum_digit(n)
    return answer 