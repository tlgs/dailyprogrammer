/* 05/01/2017 */

function atbash(input){
    letters = "abcdefghijklmnopqrstuvwxyz".split("").reverse();
    return input.split("").map(function(a){
        if(/[a-z]/i.test(a)){
            return a === a.toLowerCase() ?
                   letters[a.charCodeAt(0) - 97] :
                   letters[a.charCodeAt(0) - 65].toUpperCase();
        }
        return a;
    }).join("");
}
