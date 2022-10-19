CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 1) 이름과 나이 조회하기
SELECT first_name, age FROM users;

-- 2) 전체 데이터 조회하기
SELECT * FROM users;

-- 3) rowid 컬럼 조회하기
SELECT rowid, first_name FROM users;

-- 4) 이름과 나이를 나이가 어린 순으로 조회
SELECT first_name, age FROM users ORDER BY age;

-- 5) 이름과 나이를 나이가 많은 순으로 조회
SELECT first_name, age FROM users ORDER BY age DESC;

-- 6) 이름, 나이, 계좌 잔고를 나이가 어린 순으로, 같은 나이라면 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;

-- 7) 모든 지역 조회하기
SELECT country FROM users;

-- 8) 모든 지역 중복 없이 조회하기
SELECT DISTINCT country FROM users;

-- 9) 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users ORDER BY country DESC;

-- 10) 이름과 지역 중복 없이 모든 이름과 지역 조회하기 - 두 컬럼을 하나의 집합으로 보고 중복을 제거한다.
SELECT DISTINCT first_name, country FROM users;

-- 11) 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30;

-- 12) 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;

-- 13) 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

-- 14) 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name FROM users WHERE first_name LIKE '%준';

-- 15) 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';

-- 16) 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age LIKE '2_';

-- 17) 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';

-- 18) 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');

-- 19) IN 연산자 대신 OR 연산자 사용
SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';

-- 20) 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

-- 21) 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;

-- 22) AND 연산자를 사용하여 동일한 결과 반환 가능
SELECT first_name, age FROM users WHERE 20 <= age AND age <= 30;

-- 23) 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;

-- 24) OR 연산자를 사용하여 동일한 결과 반환 가능
SELECT first_name, age FROM users WHERE 20 > age OR age > 30;

-- 25) 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10;

-- 26) 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

-- 27) 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age FROM users ORDER BY age LIMIT 5;

-- 28) 11번째부터 20번째 데이터의 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;

-- 29) users 테이블의 전체 행 수 조회하기
SELECT COUNT(*) FROM users;

-- 30) 나이가 30살 이상인 사람들의 평균 나이 조회하기
SELECT AVG(age) FROM users WHERE age >= 30;

-- 31) 각 지역별로 몇 명씩 살고 있는지 조회하기 - country 컬럼으로 그룹화, 그룹 별로 포함되는 데이터의 수를 구한다.
SELECT country, COUNT(*) FROM users GROUP BY country;

-- 32) 각 성씨가 몇 명씩 있는지 조회하기, AS 구문으로 COUNT(*)였던 컬럼 명을 number_of_name으로 변경할 수 있다.
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;

-- 33) 인원이 가장 많은 성씨 순으로 조회하기
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name ORDER BY number_of_name DESC;

-- 34) 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users GROUP BY country;


-- CREATE
CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- 단일 행 삽입
INSERT INTO classmates (name, age, address)
VALUES('홍길동', 23, '서울');
-- INSERT INTO classmates
-- VALUES('홍길동', 23, '서울'); 과 같은 구문이다.

-- 여러 행 삽입
INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정
UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;

-- 5번 데이터 삭제하기
DELETE FROM classmates WHERE rowid = 5;

-- 삭제 확인
SELECT rowid, * FROM classmates;

-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;