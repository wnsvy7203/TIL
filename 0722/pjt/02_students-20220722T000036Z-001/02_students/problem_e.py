import json


def dec_movies(movies):
    r = []

    for i in range(len(movies)):
        idm = open('data/movies/'+str(movies[i].get("id"))+'.json', encoding='utf-8')
        idm2 = json.load(idm)
        # id 에 맞게 1대 1 load
        
        if idm2["release_date"][5] == '1' and idm2["release_date"][6] == '2':
            r.append(idm2["title"])

    return r

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
