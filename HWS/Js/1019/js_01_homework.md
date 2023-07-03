# JavaScript 기초

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.
   - let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다.
     - `F`: var로 변수 선언할 경우 재선언이 가능하고, 그로 인해 호이스팅이 일어날 가능성이 있다는 점에서 유일한 차이점이라고 할 수 없다.
   - "값이 없음"을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다.
     - `F`: null은 object가 반환된다.
   - for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로 활용한다.
     - `F`: 객체의 속성을 순회할 때 사용되며, 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장되지 않는다.
   - '==' 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true, 아니면 false를 반환한다.
     - `F`: 동등연산자는 암묵적 형 변환 이후에 두 변수의 값을 비교하고 같다면 true, 아니면 false를 반환한다.

2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오.

   ```js
   const numbers = [1, 2, 3, 4, 5]
   ```

   - for ... of 문을 사용하여 배열의 각 요소를 출력하시오.

     ```js
     const numbers = [1, 2, 3, 4, 5]
     
     for (const num of numbers) {
         console.log(num)
     }
     
     // 1
     // 2
     // 3
     // 4
     // 5
     ```

   - for ... of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생성하시오.

     ```js
     const numbers = [1, 2, 3, 4, 5]
     
     const nums = []
     
     numbers.forEach(function(num) {nums.push(num + 10)})
     
     console.log(nums)
     
     // [ 11, 12, 13, 14, 15 ]

   - for ... of 문을 사용하여 배열의 각 요소들 중 홀수 요소들로만 구성된 새로운 배열을 생성하시오.

     ```js
     const numbers = [1, 2, 3, 4, 5]
     
     const odd_nums = numbers.filter(function(num) {
         return num % 2 === 1
     })
     
     console.log(odd_nums)
     
     // [ 1, 3, 5 ]
     ```

   - for ... of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오.

     ```js
     const numbers = [1, 2, 3, 4, 5]
     
     // 1
     let sum = 0
     
     for (const num of numbers) {
         sum += num
     }
     
     // 2
     const sum_a = numbers.reduce(function (total, num) {
         return total + num
     })
     
     console.log(sum)
     console.log(sum_a)
     
     // 15
     ```

