/* 19/01/2016 */

var x;

for(x = 99; x > 1;){
  console.log(x + " bottles of beer on the wall, " + x + " bottles of beer.");
  if(x == 2)
    console.log("Take one down and pass it around, " + --x + " bottle of beer on the wall.\n");
  else
  console.log("Take one down and pass it around, " + --x + " bottles of beer on the wall.\n");
}
// 1 case
console.log(x + " bottle of beer on the wall, " + x + " bottle of beer.");
console.log("Take one down and pass it around, no more bottles of beer on the wall.\n");
//no bottles case
console.log("No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.");
