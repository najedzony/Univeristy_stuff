function * fib(){
    var [a, b] = [0, 1];
    while(true){
        yield a;
        [a, b] = [b, a + b];
    }
}

function* take(f, n){
    for(var i = 0; i < n; i++){
        let next = f.next();
        yield next.value
    }
}

for (let num of take(fib(), 10)){
    console.log(num);
}