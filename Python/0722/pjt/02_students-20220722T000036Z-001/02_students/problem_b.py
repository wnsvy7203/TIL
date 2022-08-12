import json
from pprint import pprint


def movie_info(movie, genres):
    new_data = {
        'id': movie.get("id"),
        'title': movie.get("title"),
        'poster_path': movie.get("poster_path"),
        'vote_average': movie.get("vote_average"),
        'overview': movie.get("overview"),
        'genre_ids': movie.get("genre_ids")
    }
    genre_list = []    # genre_list 생성
    for genre in genres:    
        for i in range(len(new_data['genre_ids'])):
# genres 데이터의 "id" 값과 genre_ids 의 데이터 값이 같으면,
# genres 데이터의 "name"을 출력
# 출력된 "name" 값을 genre_list에 추가하고
# new_data['genre_ids']의 데이터를 new_data['genre_names']로 대체함.

            if new_data['genre_ids'][i] == genre.get("id"):
                genre_list.append(genre.get("name"))
    new_data['genre_games'] = genre_list
    
    del new_data['genre_ids']

    return new_data

    # genres.json을 이용하여 genre_ids를
    # 각 장르 번호에 맞는 name 값으로 대체한 genre_names 키 생성

     
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
