function fib(n){
    if(n <= 1){
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

function memo(func){
    tab = {}
    return function(n){
        if(!tab[n]){
            tab[n] = func(n);
        }
        return tab[n];
    }
}

fib = memo(fib);

function measureTime(i, f, label) {
    console.time(label);
    console.log("fib(" + i + ") = " + f(i));
    console.timeEnd(label);
}

function fibbiter(n)
{
    let f0 = 0;
    let f1 = 1;
    let pom = 0;
    for(let i = 1; i < n; i++)
    {
        pom = f0;
        f0 = f1;
        f1 += pom;
    }
    return f1;
}

const n = 97;
measureTime(n, fibbiter, "fibonacci_iteracyjny");
measureTime(n, fib, "fibonacci_spamiętywany");
