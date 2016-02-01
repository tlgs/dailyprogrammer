/* 20/01/2016 */

function version1(input){
  var i;

  input = input.split(" ");

  for(i = 0; i < input.length; i++){
  if(isNaN(parseInt(input[i])))
    input.splice(i--,1);
  else
    input[i] = parseInt(input[i]);
  }

  input.sort(function(a, b){return a-b});

  for(i = 0; i < input.length; i++ )
    console.log(input[i]);
}

function version2(input){
  var = nums = [], str = [], output = [],
        i;

  input = input.split(",");

  for(i=0; i < input.length; i++){
    if( !isNaN(+input[i]) )
      nums.push(parseInt(input[i]));
    else
      str.push(input[i]);
  }

  nums.sort(function(a, b){return a-b});
  str.sort(function(a, b){return a.toLowerCase().localeCompare(b.toLowerCase)});

  output = nums.concat(str);

  for(i=0; i < output.length; i++)
    console.log(output[i]);
  
}

var input = prompt("Please input a series of digits/strings, limited by a comma:"),
