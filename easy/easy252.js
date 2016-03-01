/* 01/02/2016 */

//Brute-force implementation
function nightStash(s, c){

  for(var i = 0; i < s; i++){
    if(c % s !== 1 || Math.floor( c/s ) == 0) return null;
    c -= (Math.floor( c/s ) + 1);
  }
  return c;
}

var sailors = prompt("How many sailors are stranded in the isle?"),
    test,
    coconuts = 1;

while(true){
  test = nightStash(sailors, coconuts);
  if( test !== null && (test % sailors === 0))
    break;
  else
    coconuts ++;
}

console.log(sailors + " sailors need " + coconuts + " coconuts!" );
