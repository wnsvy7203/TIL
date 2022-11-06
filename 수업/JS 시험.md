# JS 시험

## 기초

### 변수와 식별자

- 식별자 정의와 특징
  - 대소문자를 구별한다. 클래스명 외에는 모두 소문자로 시작
  - 카멜 케이스
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스
    - 상수(constants)에 사용: 개발자의 의도와 상관없이 변경될 가능성이 없는 값
- 변수 선언 키워드
  - let
    - 블록 스코프 지역 변수 선언
    - 재할당 가능 & 재선언 불가능
  - const
    - 블록 스코프 읽기 전용 상수 선언
    - 재할당 불가능 & 재선언 불가능
  - var
    - 변수 선언
    - 호이스팅 이슈로 인해 미사용 권장
      - 변수를 선언 이전에 참조할 수 있는 현상
      - var로 선언된 변수는 선언 이전에 참조할 수 있으며, 이러한 현상을 호이스팅이라고 한다.
      - 변수 선언 이전의 위치에서 접근할 경우 undefined를 반환
    - let과 const는 호이스팅이 일어나면 에러 발생

### 데이터 타입

- 원시 타입
  - Number
    - NaN(Not A Number)
    - Number.isNaN(Number이면 true, 아니면 false)
  - String
    - Template Literal을 사용하면 줄 바꿈 되며, 문자열 사이에 변수도 삽입 가능
  - Boolean
  - Empty Value(undefined, null)
    - 동일한 역할을 하지만 JavaScript의 설계 실수로 두 개의 키워드가 존재한다.
    - null: 변수의 값이 없음을 의도적으로 표현할 때 사용, `typeof null`사용 시, object로 출력된다(설계 당시의 버그).
    - undefined: 변수 선언 이후 값을 할당하지 않으면 자동으로 undefined 할당
  - Symbol

- 참조 타입

### 연산자

- 동등 연산자(==)
  - 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교

### 조건문

- switch statement
  - 조건 표현식의 결괏값이 어느 값(case)에 해당하는지 판별
  - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용

### 반복문

- for ... in
  - 객체의 속성을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않는다.
- for ... of
  - 반복 가능한 객체를 순회할 때 사용
  - 반복 가능한 객체의 종류 Array, Set, String
  - for ... in은 속성 이름을 통해 반복 / for ... of는 속성 값을 통해 반복

### 함수

- 매개변수와 인자의 개수 불일치 허용
  - 매개변수보다 인자의 개수가 적을 경우 undefined
- Spread syntax
  - 배열의 경우 요소, 함수의 경우 인자로 확장 가능
- 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅 발생 - 함수 호출 이후에 선언해도 동작
- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
  - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름
- 화살표 함수
  - function 키워드 생략 가능
  - 매개변수가 하나 뿐이라면 매개변수의 () 생략 가능
  - 함수 내용이 한 줄이라면 {} 와 return 도 생략 가능

### Array와 object

#### Array

- reverse: 원본 배열의 요소들의 순서를 반대로 정렬

- push & pop: 배열의 가장 뒤에 요소를 추가 또는 제거

- unshift & shift: 배열의 가장 앞에 요소를 추가 또는 제거

- includes: 배열의 특정 값이 존재하는지 판별 후 참/거짓 반환

- indexOf: 배열에 특정 값이 존재하는지 판별 후 인덱스 반환 - 요소가 없을 경우 -1 반환

- join: 배열의 모든 요소를 구분자를 이용하여 연결: 구분자 생략 시 쉼표 기준

- forEach: 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행

  - 콜백 함수는 3가지 매개변수로 구성

    ``` js
    array.forEach((element, index, array) => {
    	// do something
    })
    ```

    - element: 배열의 요소
    - index: 배열 요소의 인덱스
    - array: 배열 자체



## 심화

### DOM

- window
  - 가장 최상위 객체
- document
  - DOM 조작 관련 메소드
    - document.querySelector(selector)
      - 제공한 선택자와 일치하는 element 한 개 선택
    - document.createElement: 작성한 tagName의 HTML 요소를 생성하여 반환

### Event

- Event handler - addEventListener
  - EventTarget.addEventListener(type, listener[, options])
    - type: 반응할 event 유형을 나타내는 대소문자 구분 문자열
    - listener: 지정된 타입의 Event를 수신할 객체
  - event.prevenetDafault()

### this

- 어떠한 object를 가리키는 키워드 == python의 self
- JS의 함수는 호출될 때 this르 암묵적으로 전달받는다.
  - 함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 동적으로 결정
- Nested
  - forEach의 콜백 함수에서의 this가 메소드의 객체를 가리키지 못하고 전역 객체 window를 가리킨다.
  - 단순 호출 방식으로 사용되었기 때문인데, 이를 해결하기 위해 등장한 함수 표현식이 바로 화살표 함수이다.
- 화살표 함수
  - 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킨다.
  - addEventListener 함수에서는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻하는 반면, 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩된다.
  - 따라서 addEventListener의 콜백 함수는 function 키워드 사용



## Asynchronous JS

- 비동기
  - Call Stack
    - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO), 기본적인 JavaScript의 Single Thread 작업 처리
  - Web API
    - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로 시간이 소요되는 작업을 처리
  - Task Queue
    - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
  - Event Loop
    - Call Stack과 Task Queue를 지속적으로 모니터링
    - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push
- Axios 기본 구조
  - then을 이용해서 성공하면 수행할 로직 작성
  - catch를 이용해서 실패하면 수행할 로직 작정

- 콜백 함수
  - 다른 함수의 인자로 전달되는 함수
  - 동기, 비동기 상관없이 사용 가능
  - 시간이 걸리는 비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용되는 콜백 함수를 비동기 콜백이라고 부른다.

- Promise
  - Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체