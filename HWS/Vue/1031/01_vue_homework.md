# Vue 기초

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - SPA 는 Single Pattern Application 의 약자이다.
     - `F`: Single Page Application의 약자이다.
   - SPA 는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고 , 이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.
     - `T` 
   - Vue.js 에서 말하는 '반응형'은 데이터가 변경되면 이에 반응하여 연결된 DOM 이 업데이트되는 것을 의미한다.
     - `T`
   - v-bind 디렉티브는 `@`, v-on 디렉티브는 `:` shortcut(약어)을 제공한다.
     - `F`: v-on 디렉티브가 제공하는 약어가 `@`, v-bind 디렉티브가 제공하는 약어가 `:`이다.
   - v-model 디렉티브는 input, textarea , select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.
     - `F`: Vue instance와 DOM의 양방향 바인딩을 이룬다.

2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

   - Model: 실제 데이터(JSON)
   - View: 눈에 보이는 부분(DOM)
   - View-Model(Vue)
     - View를 위한 Model
     - View와 연결(binding)되어 Action을 주고 받는다.
     - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경된다.
     - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경된다.

3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

   ```html
   <div id='app'>
       {{ __(a)__ }}
   </div>
   
   <script>
   	const app = __(b)__({
           el: __(c)__,
           data: {
           	message: 'Hello World',
       	}
       })
   </script>
   ```

   - (a): `message`
   - (b): `new Vue`
   - (c): `'#app'`