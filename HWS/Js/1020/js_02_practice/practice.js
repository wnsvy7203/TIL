const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

// solution 함수 완성
function createZeroArray(len) {
  return new Array(len).fill(0)
}

function solution(K, N, M, chargers) {
  let arr = createZeroArray(N+1)
  
  for (const i of chargers) {
    for (let j = 1; j <= N; j++) {
      if (j === i) {
        arr[j] = 1
      }
    }
  }

  let bus = 0
  let cnt = 0

  while (true) {
    let new_arr = arr.slice(1, K+1)
    if (new_arr.includes(1) === false) {
      cnt = 0
      break
    }

    for (let a = K; a >= 0; a--) {
      if (arr[a] === 1) {
        cnt += 1
        arr = arr.slice(a, N+1)
        bus += a
        break
      }
    }

    if ( bus + K >= N ) {
      break
    }
  }

  return console.log(cnt)
}

for (const input of inputs) {
  solution(...input)
}