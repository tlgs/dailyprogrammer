/* 18/12/2016 */

function drawBoard(rows, cols, width, height){
    var output = "";

    for(var i = 0; i < rows; i++){
        for(var j = 0; j < (width + 1) * cols + 1; j++){
            output += "*";
        }
        output += "\n";
        for(var j = 0; j < height; j++){
            for(var k = 0; k < cols; k++){
                output += "*";
                if( (!(i%2) && k%2) || (i%2 && !(k%2)) ){
                    for(l = 0; l < width; l++){
                        output += "#";
                    }
                }else{
                    for(l = 0; l < width; l++){
                        output += " ";
                    }
                }
            }
            output += "*\n";
        }
    }

    for(var j = 0; j < (width + 1) * cols + 1; j++){
        output += "*";
    }

    console.log(output);
}
