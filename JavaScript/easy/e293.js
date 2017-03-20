/* 08/12/2016 */

var rules = {
  white:  ["red", "orange", "green", "purple"],
  red:    ["green"],
  black:  ["red", "black", "purple"],
  orange: ["red", "black"],
  green:  ["orange", "white"],
  purple: ["red", "black"]
};

function defuse (wires){
  while(wires.length > 1){
    if(! rules[wires.shift()].includes(wires[0]))
      return "Boom!";
  }
  return "Bomb defused!";
}
