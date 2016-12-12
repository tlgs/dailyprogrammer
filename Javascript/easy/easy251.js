/* 26/01/2016 */

//Output is not correct.
function tableify(input){
  var i,
      j,
      table = [];

  for(i=0; i < input.length; i++){
    table[i] = [];

    for(j=0; j< input[i].length; j++)
      table[i][j] = input[i].charAt(j);
  }

  return table;
}

function deconstruct(input){
  var numRows = input.length,
      numCol = input[0].length,
      rows = [],
      col = [],
      rowFlag = false,
      colFlag = false,
      rowCount = 0,
      colCount = 0,
      maxRowCount = 0,
      maxColCount = 0;

  for(i=0; i < numRows; i++)
    rows[i] = [];

  for(j=0; j < numCol; j++)
    col[j] = [];

  for(i=0; i < numRows; i++){
    for(j=0; j < numCol; j++){
      if(input[i][j] == '*'){
        if(rowFlag)
            rows[i][rowCount-1]++;
        else {
            rowCount++;
            rows[i][rowCount-1] = 1;
        }
        rowFlag = true;
      }
      else
        rowFlag = false;
    }
    rowCount > maxRowCount ? maxRowCount = rowCount : "" ;
    rowCount = 0;
    rowFlag = false;
  }

  for(j=0; j < numCol; j++ ){
    for(i=0; i < numRows; i++){
      if(input[i][j] == '*'){
        if(colFlag)
            col[j][colCount-1]++;
        else {
            colCount++;
            col[j][colCount-1] = 1;
        }
        colFlag = true;
      }
      else
        colFlag = false;
    }
    colCount > maxColCount ? maxColCount = colCount : "" ;
    colCount = 0;
    colFlag = false;
  }

  var rowStr = [],
      colStr = [];

  for(i = maxColCount; i > 0; i--){
    colStr[maxColCount - i] = "";
    for(j=0; j < numCol; j++){
      if(col[j][i-1] === undefined)
        col[j][i-1] = " ";
      colStr[maxColCount - i] += col[j][i-1] + " ";
    }
  }

  for(i=0; i < numRows; i++){
    rowStr[i] = "";
    for(j=maxRowCount; j > 0; j--){
      if(rows[i][j-1] === undefined)
        rows[i][j-1] = " ";
      rowStr[i] += rows[i][j-1] + " ";
    }
  }

  console.log("Columns:");
  for(i=0; i < colStr.length; i++){
    console.log(colStr[i]);
  }

  console.log("Rows:");
  for(i=0; i < rowStr.length; i++){
      console.log(rowStr[i]);
  }

}

input1 = ["    *", "   **", "  * *", " *  *", "*****"];
input2 = ["    ** *  ", "   *****  ", "  ******  ", " ******** ", "**********", " *      * ", " * ** * * ", " * ** * * ", " * **   * ", " ******** "];

deconstruct(tableify(input1));
