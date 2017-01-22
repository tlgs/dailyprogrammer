/* 10/03/2016 */

function addLargestSquares(a, b, c){
  arr = [a, b, c].sort(function(a, b){return b-a});
  return arr[0]*arr[0] + arr[1]*arr[1];
}
