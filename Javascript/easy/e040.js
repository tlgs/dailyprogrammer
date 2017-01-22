/* 14/04/2016 */
// http://stackoverflow.com/questions/3746725/create-a-javascript-array-containing-1-n

Array.apply(null, { length: 1000 }).map((_, i) => console.log(i+1));
