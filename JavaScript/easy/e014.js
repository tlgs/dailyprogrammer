/* 18/02/2016 */

function blockReverse(input, k){
  var i, output=[];

  for(i=0; i < input.length; i += k)
    output.push(input.slice(i, i + k).reverse());

  return output;
}
