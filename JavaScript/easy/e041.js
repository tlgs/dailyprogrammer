/* 14/04/2016 */

var input = prompt("Please enter a sentence:");

for(var line ="*", pad="*", i=0; i < input.length+2; i++){
  line+="*";
  pad+=" ";
}
line+="*\n";
pad+="*\n";

console.log(line + pad + "* " + input + " *\n" + pad + line);
