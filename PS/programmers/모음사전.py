def solution(word):
    dictionary = []
    for i in range(1, 6):
        dictionary = dictionary + list(product(["A","E","I","O","U"], i))
    
    for idx, w in enumerate(sorted(dictionary)):
        if word == ''.join(w):
            return idx + 1
        

def product(arr, length):
    for i in range(len(arr)):
        if length == 1:
            yield [arr[i]]
        else:
            for word in product(arr, length - 1):
                yield [arr[i]] + word