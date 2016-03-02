/* 01/02/2016 */

function dayOfYear(day, month){
  var numberDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
      count = 0;

  for(var i=0; i < month - 1; i++)
    count += numberDays[i];

  return count + day;
}
