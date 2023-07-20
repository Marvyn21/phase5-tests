// reverse string
// function reversedString(mystring){
//     let array_string = mystring.split("");
//     array_string.reverse();
//     console.log(array_string.join(""))
//     return array_string.join("");
// }
// reversedString("lisa")

function arrayNums(num_array){
    let max_num = num_array[0];
    for (let i = 0; i < num_array.length; i++){
        if (num_array[i] > max_num){
            max_num = num_array[i];
        }
    }
    console.log(max_num)
}
arrayNums(['4', '5', '8', '2', '90'])