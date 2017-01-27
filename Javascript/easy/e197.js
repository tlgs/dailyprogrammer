function ISBNvalidator(input){
    return input.replace(/-/g,'').split('').reduce((a, b, i) => b == "X" ?
                                                  a + 10 :
                                                  a + (10-i)*parseInt(b, 10), 0)
                                                  % 11 == 0;
}
