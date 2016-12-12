/* 28/02/2016 */

function breakInHalf(input){
  var top = [], length = input.length;

  for(var i=0; i < Math.floor(length/2); i++){
    top.push(input.shift());
  }

  return [top, input];
}
