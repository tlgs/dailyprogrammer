/* 08/12/2016 */

function scrabble(letters, word){
    letters = letters.split('');
    for(var i = 0; i < word.length; i++){
        var j = letters.indexOf((word.charAt(i)));
        if(j === -1 && letters.indexOf("?") > -1){
            letters.splice(letters.indexOf("?"), 1)
        } else if(j === -1){
             return false;
        } else{
            letters.splice(j, 1);
        }
    }
    return true;
}
