/* 09/01/2017 */

function countBulbs(input){
    input = input.split(/[ \n]/);
    for(var i = 0, bulbs = []; i < input[0]; i++){
        bulbs[i] = false;
    }
    for(i = 1; i < input.length; i += 2){
        for(j = Math.min(input[i], input[i+1]); j <= Math.max(input[i], input[i+1]); j++){
            bulbs[j] = !bulbs[j];
        }
    }
    return bulbs.reduce((a,b) => a + (b ? 1:0));
}
