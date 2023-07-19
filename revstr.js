// reverse string
function reversedString(mystring){
    let array_string = mystring.split("");
    array_string.reverse();
    console.log(array_string.join(""))
    return array_string.join("");
}
reversedString("lisa")
