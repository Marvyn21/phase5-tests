function solution(letters) {
    const seenLowerCase = new Set();
    let count = 0;
  
    for (let i = 0; i < letters.length; i++) {
      const char = letters[i];
      const lowerChar = char.toLowerCase();
  
      if (char === lowerChar && !seenLowerCase.has(lowerChar)) {
        seenLowerCase.add(lowerChar);
        count++;
      }
    }
  
    return count;
  }
  

//   function isPalindrome(some_string){
//     const new_string = some_string.toLowerCase().replace(/[^a-z0-9]/g, '');

//     console.log(new_string)
//     console.log(new_string === new_string.split("").reverse().join(""));
//   }

// isPalindrome("race a car")

function reverse(str){
    let rev_str = '';
    for (let i = str.length - 1; i>=0; i--){
        rev_str += str[i];
    }
    return rev_str
}

function checker(str){
    const reverse_string = reverse(str);

    if(str === reverse_string){
        console.log("is palindrome")
    }
    else{
        console.log("is not a palindrome")
    }

}
checker("bbob")