def solution(genres, plays):
    answer = []
    total = {}
    
    # 1. genre의 총 play 수 계산하는 total dict 만들기
    for genre, play in zip(genres, plays):
        if genre not in total:
            total[genre] = play
        else:
            total[genre] += play
    
    # 2. 정렬
    # play 수로 내림차순 정렬
    # [('pop', 3100), ('classic', 1450)]
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    # play 수로 내림차순 정렬
    # [('pop', (4, 2500)), ('pop', (1, 600)), ('classic', (3, 800)), ('classic', (0, 500)), ('classic', (2, 150))]
    genre_play= sorted(list(zip(genres, enumerate(plays))), key=lambda x: (x[0], x[1][1]), reverse=True)
    
    # 3. answer에 해당하는 인덱스 추가
    # play 수가 많은 genre부터 꺼내서 
    for key, value in total:
        count = 0  # genre당 2개만 넣기 위해 count 변수 설정
        for genre, (i, play) in genre_play:
            if key == genre: # genre와 total에 있는 genre와 일치하면
                answer.append(i) # index answer에 append
                count += 1
                if count == 2: # genre당 2개가 되면 멈추기
                    break 
    return answer