/* 04/01/2017 */

function cull(input){
    return input.split(' ').filter((a, i, b) => b.indexOf(a) == i).join(' ');
}


console.log(cull("3 1 3 4 4 1 4 5 2 1 4 4 4 4 1 4 3 2 5 5 2 2 2 4 2 4 4 4 4 1"));
console.log(cull("1 1 2 2 3 3 4 4"));
