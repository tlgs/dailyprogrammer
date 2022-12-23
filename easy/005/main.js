/* 17/01/2016 */

var correctUser = "hayhay",
    correctPass = "password1";

var user = prompt("Username:");
var password = prompt("Password:");

(user === correctUser && password === correctPass) ? alert("Welcome to this useless program!") : alert("Access Denied!");
