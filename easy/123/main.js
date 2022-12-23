/* 06/01/2017 */

function sumDigits(input){
    if(input.toString().length === 1)
        return input;
    else
        return sumDigits(input.toString().split('').reduce((a, b) => a + parseInt(b), 0));
}
