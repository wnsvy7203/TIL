# 0901 Homework

## Model

1. Model 반영하기
    - `migration`

2. Model 변경사항 저장하기
    1. Model의 변경사항을 저장하기 위한 명령어 작성
        - `makemigrations`로 migration 파일(설계도) 생성
        - `migrate`로 DB 반영(모델 <-> DB 동기화)
    2. `sqlmigrate`
        - 해당 migration 파일이 SQL 문으로 어떻게 해석될 지 미리 확인 가능

3. Python Shell
    - `python -i`

4. Django Model Field
    ```python
        class AutoField(**options)
        class BigAutoField(**options)
        class BigIntergerField(**options)
        class BinaryField(max_length=None, **options)
        class CharField(max_length=None, **options)
        class DateTimeField(auto_now=False, auto_now_add=False, **options)
    ```