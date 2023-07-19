function longest_consec(strarr, k) {
    const n = strarr.length;
  
    // Check for edge cases
    if (n === 0 || k <= 0 || k > n) {
      return "";
    }
  
    let longestConcatenation = "";
  
    for (let i = 0; i <= n - k; i++) {
      const currentConcatenation = strarr.slice(i, i + k).join("");
      if (currentConcatenation.length > longestConcatenation.length) {
        longestConcatenation = currentConcatenation;
      }
    }
    return longestConcatenation;
  }
  
str = ["tree"],
str = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
t = 2
console.log(longest_consec(str, t))