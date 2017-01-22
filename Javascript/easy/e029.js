/* 03/03/2016 */
/* revisited 25/03/2016 */

function palindrome(str) {
  var newStr = str.replace(/[\W_]/g, '').toLowerCase();
  return (newStr === newStr.split('').reverse().join('')) ? true : false;
}
