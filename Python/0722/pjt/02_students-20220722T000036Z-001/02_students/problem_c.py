import json
from pprint import pprint


def movie_info(movies, genres):
    # new_data 여러 개를 list화해서 출력
    import problem_b

    data = []
    for i in range(len(movies)):
        data.append(problem_b.movie_info(movies[i], genres))

    return data
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
