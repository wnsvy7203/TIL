// console.log('hello, javascript');

function add(num1, num2) {
    return num1 + num2
}

console.log(add(2, 7))


const sub = function (num1, num2) {
    return num1 - num2
}

console.log(sub(7, 2))

const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
}

console.log(greeting())