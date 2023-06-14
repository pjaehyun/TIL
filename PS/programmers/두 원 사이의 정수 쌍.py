def solution(r1, r2):
    
    def get_y(x, r, name):
        y = (r**2 - x**2)**(1/2)
        res = int(y)
        if name == "r1" and y - res == 0:
            return res - 1
        return res
        
    answer = 0
    for i in range(1, r2):
        if i < r1:
            answer += (get_y(i, r2, "r2")) - (get_y(i, r1, "r1"))
        else:
            answer += get_y(i, r2, "r2")
    return (answer + r2 - r1 + 1)*4