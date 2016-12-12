/* 03/10/2016 */

var tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
var ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
var exception = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];

for(var i = tens.length - 1; i >= 0; i--){
  for(var j = ones.length - 1; j >= 0; j--){
    console.log(tens[i].charAt(0).toUpperCase() + tens[i].slice(1)  + "-" + ones[j] + " bottles of beer on the wall, " + tens[i] + "-" + ones[j] + " bottles of beer.");
    if(j > 0)
      console.log("Take one down and pass it around, " + tens[i] + "-" + ones[j-1] + " bottles of beer on the wall.");
    else{
      console.log("Take one down and pass it around, " + tens[i] + " bottles of beer on the wall.");
      console.log(tens[i].charAt(0).toUpperCase() + tens[i].slice(1)  + " bottles of beer on the wall, " + tens[i] + " bottles of beer.");
      if(i > 0)
        console.log("Take one down and pass it around, " + tens[i-1] + "-" + ones[ones.length - 1] + " bottles of beer on the wall.");
      else
        console.log("Take one down and pass it around, " + exception[exception.length - 1] + " bottles of beer on the wall.");
    }
  }
}

for(var i = exception.length - 1; i >= 0; i--){
  console.log(exception[i].charAt(0).toUpperCase() + exception[i].slice(1) + " bottles of beer on the wall, " + exception[i] + " bottles of beer.");
  if(i > 0)
    console.log("Take one down and pass it around, " + exception[i - 1] + " bottles of beer on the wall.");
  else
    console.log("Take one down and pass it around, " + ones[ones.length - 1] + " bottles of beer on the wall.");
}

for(var i = ones.length - 1; i >= 1; i--){
    console.log(ones[i].charAt(0).toUpperCase() + ones[i].slice(1) + " bottles of beer on the wall, " + ones[i] + " bottles of beer.");
    if(i > 1)
    console.log("Take one down and pass it around, " + ones[i - 1] + " bottles of beer on the wall.");
}

console.log("Take one down and pass it around, " + ones[0] + " bottle of beer on the wall");
console.log("One bottle of beer on the wall, one bottle of beer.");
console.log("Take one down and pass it around, no more bottles of beer on the wall.");
console.log("No more bottles of beer on the wall, no more bottles of beer. ");
console.log("Go to the store and buy some more, ninety-nine bottles of beer on the wall.");
