/* 03/03/2016 */

//My experience with C kicks in:
function isPalindromeOldSchool(input){
  input = input.split("");
  var middle = Math.floor(input.length / 2);
  if(input.length % 2)  input.splice(middle, 1);
  for(i = 0; i < middle; i++)
    if(input[middle + i] !== input[middle - i - 1]) return false;

  return true;
}

//Something more JS appropriate (takes care of whitespace/symbols):
function isPalindrome(input){
  input = input.split("");
  var re = /\W/g, match;

  while(match = re.exec(input.join(""))){
    input.splice(match.index, 1);
    re.lastIndex --;
  }

  return (input.join("") == input.reverse().join("") ) ? true : false;
}
