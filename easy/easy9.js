/* 20/01/2016 */

var input = prompt("Please input a series of digits:"),
    i;

input = input.split(" ");

for(i = 0; i < input.length; i++){
  if(isNaN(parseInt(input[i])))
    input.splice(i--,1);
  else
    input[i] = parseInt(input[i]);
}

input.sort(function(a, b){return a-b});

for(i = 0; i < input.length; i++ ){
  console.log(input[i]);
}
