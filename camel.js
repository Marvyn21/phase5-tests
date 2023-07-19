// function camelCase(str){
//     const array = str.split(" ").map((word) => {
//         return word.slice(0,1).toUpperCase() + word.slice(1)
//     })
//     console.log(array.join(""))
//     return array.join("")
// }

// camelCase("camel case word")


// // area of a circle
// function areaCircle(r){
//     console.log(Math.PI * (Math.pow(r,2)))
//     return Math.PI * Math.pow(r,2)
// }
// areaCircle(2)

// // multiples 
// function multiples(m, n){
//     let arr = []
//     for(let i=1; i<=m; i++){
//         arr.push(i * n)
//     }
//     console.log(arr)
//     return arr
// }
// multiples(4, 5)


function fizzBuzz(n){
    for(i=1; i <= n; i++){
        if(i % 3 === 0 && i % 5 === 0){
            console.log("FizzBuzz")
        }
        else if(i % 3 === 0){
            console.log("Fizz")
        }
        else if(i % 5 === 0){
            console.log("Buzz")
        }
        else{
            console.log(i)
        }
    }
}

fizzBuzz(75)