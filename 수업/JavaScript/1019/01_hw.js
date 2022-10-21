for (let i = 0; i < 5; i++) {
  str1 = ''
  str2 = ''
  for (let j = 0; j < 4 - i; j++){
    str1 += ' '
  }
  for (let j = 1; j <= 2*i+1; j++){
    str2 += '*'
  }
  console.log(str1+str2)
}
