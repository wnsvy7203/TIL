import json


def max_revenue(movies):
    a = []
    rev = []
    for i in range(len(movies)):
        # id 에 맞게 1대 1 load
        idm = open('data/movies/'+str(movies[i].get("id"))+'.json', encoding='utf-8')
        idm2 = json.load(idm)
        a.append(idm2)
        rev.append(idm2["revenue"])
        
        cnt = rev[0]
        n = 0
        for j in range(1, len(rev)):
    # movies에서 vote_count의 값들만 따로 모아,
    # 첫 번째 요소부터 차례로 값을 비교하면서 최대값을 구하고
    # 그 요소에 해당하는 "title"을 출력
            if cnt < rev[j]:
                cnt = rev[j]
                n = j
    title = a[n].get("title")
    return title
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
