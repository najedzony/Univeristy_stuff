function sum(){
    var sum = 0;
    for(var arg of arguments){
        sum += arg;
    }
    return sum;
}

console.log(sum(1, 2, 3));
console.log(sum(1, 2, 3, 4, 5));

