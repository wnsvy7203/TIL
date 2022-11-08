# Vue 주요 내용 정리

## Front-end Development

- SPA(Single Page Application)
  - 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
    - CSR 방식으로 요청을 처리하기 때문이다.
- SSR(Server Side Rendering)
  - 서버가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
  - 전달받은 새 문서를 보기 위해 브라우저 새로고침 필요
- CSR(Client Side Rendering)
  - 최초 한 장의 HTML을 받아오는 것은 같지만, 서버로부터 최초로 받아오는 문서는 빈 html 문서이다.
  - 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간 소요
  - 검색 엔진 최적화가 어렵다.
- CSR vs SSR
  - 이런 장단점 때문에 SPA 서비스에서도 SSR을 지원하는 프레임워크가 발전하고 있다.

## Vue

### MVVM Pattern

- View: 우리 눈에 보이는 부분 = DOM
- Model: 실제 데이터 = JSON
- View Model(Vue)
  - View를 위한 Model
  - View와 연결(binding)되어 Action을 주고 받는다.
  - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경된다.
  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경된다.

### `el`(element)

- Vue instance와 DOM 을 mount(연결)하는 옵션
  - View와 Model을 연결하는 역할
  - HTML id 혹은 class와 마운트 가능
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않는다.
  - Vue 속성 및 메소드 사용 불가

### `data`

- Vue instatnce의 데이터 객체 혹은 인스턴스 속성
  - 반드시 기본 객체 `{}(object)`여야 한다.
  - 정의된 속성은 `interpolation {{ }}`을 통해 view에 렌더링 가능

### `methods`

- Vue instance의 method들을 정의하는 곳
  - 메소드 정의 시, 화살표 함수는 사용 불가
  - 화살표 함수의 this는 함수가 선언될 때 상위 스코프를 가리킨다.
    - 따라서 methods의 상위 스코프인 window를 가리키게 되고, this로 Vue의 data를 변경하지 못한다.

### Syntax

- 렌더링 된 DOM을 기본 Vue in