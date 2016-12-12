/* 08/12/2016 */

function scrabble(letters, word){
  for(var i = 0; i < word.length; i++){
    var j = letters.indexOf((word.charAt(i)));
    if(j === -1)
      return false;
    letters.splice(j, 1);
  }
  return true;
}
