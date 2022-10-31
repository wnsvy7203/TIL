# GIT

## Git undoing

- 개요
  - Working Directory 작업 단계
    - Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
    - git restore
  - Staging Area 작업 단계
    - Staging Area에 반영된 파일을 Working Directory로 되돌리기
    - git rm --cached
    - git restore --staged
  - Repository 작업 단계
    - 커밋을 완료한 파일을 Staging Area로 되돌리기
    - git commit --amend

### Working Directory 작업 단계

- git restore
  - 아직 커밋되지 않은 부분을 마지막 커밋 상태로 되돌린다.

### Staging Area 작업 단계

- 개요
  - Stating Area에 반영된 파일을 

- git rm --cached
  - root-commit이 없는 경우
- git restore --staged
  - root-commit이 있는 경우

### Repository 작업 단계

- 커밋을 완료한 파일을 Staging Area로 되돌리기
  - git commit --amend

## Git reset & revert

- Git reset
  - 개요
    - 프로젝트를 특정 커밋(버전) 상태로 되돌림
    - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
    - git reset [옵션] {커밋 ID}
      - 옵션은 soft, mixed, hard 중 하나를 작성
        - soft: Staging Area로 되돌아간다.
        - mixed: Working Directory를 add 하기 전으로 unstaged로 만듦
        - hard: 모든 Working Directory 초기화
      - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성
- Git revert
  - 개요
    - 이전 커밋을 취소한다는 새로운 커밋을 생성한다.
    - git revert {커밋 ID}: 이 때 커밋 ID는 취소하고 싶은 커밋 ID 작성
- 차이점
  - 개념적 차이
    - 
  - 문법적 차이

## Git branch & merge

### Git branch

- 개요

  - 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git 도구

- 장점

  - 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전하다.
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능하다.
  - Git은 브랜치를 만드는 속도가 아주 빠르고, 적은 용량을 소모한다.

- 브랜치의 조회, 생성, 삭제와 관련한 Git 명령어

  - 조회
    - git branch: 로컬 저장소의 브랜치 목록 확인
    - git branch -r: 원격 저장소의 브랜치 목록 확인
  - 생성
    - git branch { 브랜치 이름 }: 새로운 브랜치 생성
    - git branch { 브랜치 이름 } { 커밋 ID }: 특정 커밋 기준으로 브랜치 생성
  - 삭제
    - git branch -d { 브랜치 이름 }: 병합된 브랜치만 삭제 가능
    - git branch -D { 브랜치 이름 }: 강제로 삭제

- git switch

  - 현재 브랜치에서 다른 브랜치로 이동하는 명령어
  - git switch { 브랜치 이름 }: 다른 브랜치로 이동
  - git switch -c { 브랜치 이름 }: 브랜치를 생성 후 이동
  - git switch -c { 브랜치 이름 } { 커밋 이름 }: 특정 커밋 기준으로 브랜치 생성 및 이동
  - switch하기 전에 해당 브랜치의 변경 사항을 반드시 커밋해야 한다.
    - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 된다.

  > HEAD
  >
  > - 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로, 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있다.
  > - git log 혹은 cat .git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있다.
  > - 결국 git switch는 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어이다.

### Git Merge

- fast-forward Merge

- 3-way Merge
- 2-way Merge
- Merge Conflict

## Git workflow

- 개요
  - Branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법
    - 원격 저장소 소유권이 있는 경우: Shared repository model
    - 원격 저장소 소유권이 없는 경우: Fork & Pull model

### Shared repository model

- 사용자는 자신이 작업할 기능에 대한 브랜치를 생성하고, 그 안에서 기능을 구현