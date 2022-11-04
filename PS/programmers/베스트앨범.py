from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(list)
    genre_count = defaultdict(int)
    
    for genre, play in zip(genres, enumerate(plays)):
        genres_dict[genre].append(play)
        genre_count[genre] += play[1]
    
    for key in genres_dict.keys():
        genres_dict[key].sort(key=lambda x: x[1], reverse=True)
    
    genre_sequence = sorted([(k,v) for k,v in genre_count.items()], key=lambda x:x[1], reverse=True)
    
    for genre, _ in genre_sequence:
        for _ in range(2):
            if genres_dict[genre]:
                idx, _ = genres_dict[genre].pop(0)
                answer.append(idx)
    return answer