/* 19/12/2016 */

function bitstringCount(n){
    return n.toString(2).split("").reduce( (a,b) => parseInt(a)+parseInt(b));
}
