/* 27/01/2017 */

function isKaprekar(num){
    if(num === 1) return true;
    var sq = Math.pow(num, 2);
    for(var i = 1; i < sq.toString().length; i++){
        var start = Math.floor(sq / 10 ** i),
            end =  sq % 10 ** i;
        if(start + end === Math.sqrt(sq) && end > 0) return true;
    }
    return false;
}

function getKaprekarNums(start, end){
    for(var i = start, out = ""; i <= end; i++){
        if(isKaprekar(i)) out += i.toString() + " ";
    }
    console.log(out);
}
