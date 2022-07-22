import json


def dec_movies(movies):
    a = []
    r = []
    for i in range(len(movies)):
        # id 에 맞게 1대 1 load
        idm = open('data/movies/'+str(movies[i].get("id"))+'.json', encoding='utf-8')
        idm2 = json.load(idm) 
        a.append(idm2)
        r.append(idm2["release_date"])

        n = 0
        for j in range(len(r)):
            if r[j][5] == 1 and r[j][6] == 2:
                n = j
        
        title = a[n].get("title")

    return title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
