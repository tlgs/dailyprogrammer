/* 16/12/2016 */

function goldilocks(input){
    input = input.split(' ');
    var seats = [];

    for(var i=2; i < input.length; i = i+2){
        if(parseInt(input[i]) > parseInt(input[0]) && parseInt(input[i+1]) < parseInt(input[1])){
            seats.push(i/2);
        }
    }
    
    return seats;
}
