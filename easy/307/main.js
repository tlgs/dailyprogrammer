/* 20/03/2017 */

function escapeRegExp(str) {
  return str.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
}

function encode(arr, sep){
    var re = new RegExp(escapeRegExp(sep), 'g');
    return arr.map(x => x.replace(re, sep + sep))
              .join(sep + String.fromCharCode((sep.charCodeAt()+1)%256));
}

function decode(str, sep){
    var re = new RegExp(escapeRegExp(sep + sep), 'g');
    return str.replace(re, sep)
              .split(sep + String.fromCharCode((sep.charCodeAt()+1)%256));
}
