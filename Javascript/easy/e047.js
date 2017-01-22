/* 20/12/2016 */

function caesar(input, shift){
    if(shift < 0){
        shift = (shift % 26) + 26;
    }

    input = input.split("");
    for(var i = 0; i < input.length; i++){
        var c = input[i].charCodeAt(0);

        if(input[i].match(/[A-Z]/)){
            input[i] = String.fromCharCode(65 + (c + shift - 65) % 26);
        }else if(input[i].match(/[a-z]/)){
            input[i] = String.fromCharCode(97 + (c + shift - 97) % 26);
        }
    }
    return input.join("")
}
