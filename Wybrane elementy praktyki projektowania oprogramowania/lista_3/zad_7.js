function fib(){
    var [a, b] = [0, 1];
    return{
        next : function(){
            var pom = a;
            [a, b] = [b, a + b];
            return{
                value : pom,
                done : false
            }
        }
    }
}

function * fib1(){
    var [a, b] = [0, 1];
    while(true){
        yield a;
        [a, b] = [b, a + b];
    }
}

//Niemożliwe
// for(let i of fib()){
//     console.log(i);
// }

//Możliwe
// for(let i of fib1()){
//     console.log(i);
// }