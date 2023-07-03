# SQL

## 1. SQL 용어 및 개념

아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.

```mark
기본 키, 테이블, 스키마, 레코드, 컬럼
```

1) 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술한 것 - 스키마
2) 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 - 테이블
3) 고유한 데이터 형식이 지정되는 열 - 컬럼
4) 단일 구조 데이터 항목을 가리키는 행 - 레코드
5) 각 행의 고유 값 - 기본 키



## 2. SQL 문법

아래의 (1) ~ (4) 중 DML이 아닌 것을 고르시오.

```markdown
(1) CREATE
(2) UPDATE
(3) DELETE
(4) SELECT
```

- CREATE는 데이터 정의 언어(DDL)이다. 따라서 답 (1)



## 3. Relational DBMS

- 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용되는 프로그램

- 대표적으로 SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등이 있다.



## 4. INSERT INTO

다음과 같은 스키마를 가지는 테이블이 있을 때, 보기 중 틀린 문장을 고르시오.

```sql
CREATE TABLE classmates(
	name TEXT,
    age INT,
    address TEXT
);
```

```markdown
(1)
INSERT INTO classmates (name, age, address)
VALUES('홍길동', 20, 'seoul');
(2)
INSERT INTO classmates VALUES('홍길동', 20, 'seoul');
(3)
insert into classmates
values(address='seoul', age=20, name='홍길동');
(4)
insert into classmates (address, age, name)
values('seoul', 20, '홍길동');
```

- (3)번이 틀린 문장, (4)번과 같이 고쳐 써야 한다.



## 5. 와일드카드 문자

SQL에서 사용 가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

- SQLite는 패턴 구성을 위한 두 개의 와일드카드를 제공한다.
  - % (percent): 0개 이상의 문자가 올 수 있음을 의미한다.
    - '영%' 패턴은 영으로 시작하는 모든 문자열과 일치한다(영, 영미, 영미리 등).
    - '%도' 패턴은 도로 끝나는 모든 문자열과 일치한다(도, 수도, 경기도 등).
    - '%강원%' 패턴은 강원을 포함하는 모든 문자열과 일치한다(강원, 강원도, 강원도에 살아요 등).
  - _ (underscore): 단일(1개) 문자가 있음을 의미한다.
    - '영_' 패턴은 영으로 시작하고 총 2자리인 문자열과 일치한다(영미, 영수, 영호 등).
    - '_도' 패턴은 도로 끝나고 총 2자리인 문자열과 일치한다(수도, 과도 등).

