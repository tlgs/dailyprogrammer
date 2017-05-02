/* 19/12/2016 */

function montyHall(n){
    var smart = 0, dumb = 0;
    for(var i = 0; i < n; i++){
        var doors = ["goat", "goat", "goat"];
        doors[Math.floor(Math.random()*3)] = "car";
        var smartPick = Math.floor(Math.random()*3);
        var dumbPick = smartPick;
        var doorShow = doors.indexOf("goat") == smartPick ?
                       doors.reduce((a, b, i) => b == "goat" ? i : a) :
                       doors.indexOf("goat");
        smartPick = [0, 1, 2].filter(a => a != dumbPick && a != doorShow)[0];
        dumb += doors[dumbPick]  == "car";
        smart += doors[smartPick]  == "car";
    }
    console.log("The smart player won the car " + smart + " times.\nThe dumb player won the car " + dumb + " times.");
}
