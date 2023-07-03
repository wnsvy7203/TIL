# JavaScript 심화

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다.
     - `T`
   - XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.
     - `T`
   - XHR 객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.
     - `T`
   - axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.
     - `T`

2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

   ```javascript
   console.log('hello SSAFY!')
   
   setTimeout(function () {
       console.log('I am from setTimeout')
   }, 1000)
   
   console.log('Bye SSAFY!')
   ```

   - Call Stack

     - `console.log('Hello SSAFY!')`가 들어오고, 출력

     - ````javascript 
       setTimeout(function () {
           console.log('I am from setTimeout')
       }, 1000) 가 들어오지만, Web API로 보낸다.
       ````

     - `console.log('Bye SSAFY!')`가 들어오고 출력

     - ```javascript
       setTimeout(function () {
           console.log('I am from setTimeout')
       }, 1000)의 작업이 끝나고 Call Stack에 들어온다.
       ```

     - `console.log('I am from setTimeout')` 수행(출력)

   - Web API

     - ```javascript
       setTimeout(function () {
           console.log('I am from setTimeout')
       }, 1000) 가 들어오고 1000ms가 지난 이후, Task Queue에 들어간다.
       ```

   - Task Queue

     - ```javascript
       setTimeout(function () {
           console.log('I am from setTimeout')
       }, 1000)
       작업 수행 완료된 이후, Task Queue에 들어온다.
       ```

   - Event Loop

     - Call Stack이 비어 있는 것을 체크하고`(console.log('Hello SSAFY!'), console.log('Bye SSAFY!'))` 수행 이후, 완료된 아래의 작업을 Call Stack으로 보낸다.

     - ```javascript
       setTimeout(function () {
           console.log('I am from setTimeout')
       }, 1000)
       ```