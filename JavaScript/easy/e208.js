/* 04/01/2017 */

function cull(input){
    return input.split(' ').filter((a, i, b) => b.indexOf(a) == i).join(' ');
}
