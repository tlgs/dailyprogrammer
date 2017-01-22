/* 18/12/2016 */

function txtBreak(input){
    var broken = input.split(/[\.\!\?]/g);
    var output = broken.reduce((pre, curr) => curr.length > pre.length ? curr : pre);
    console.log(output);
    console.log(output.split(" ").filter(a => a.length > 0).length);
    output = output.split(" ").map( a => a.replace(/[\,\;]/, ""));
    for(var i = 0, words = []; i < output.length; i++){
        if(output[i].length > 4){
            words.push(output[i]);
        }
    }
    console.log(words.toString());
}
