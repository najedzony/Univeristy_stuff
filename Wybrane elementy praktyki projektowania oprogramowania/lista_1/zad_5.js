function fibbrec(n)
{
    if(n <= 1)
        return n;
    return fibbrec(n - 1) + fibbrec(n - 2);
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

function measureTime(i, f, label) {
    console.time(label);
    console.log("fib(" + i + ") = " + f(i));
    console.timeEnd(label);
}

const n = 40;
for (let i = 10; i < n; i++) {
    measureTime(i, fibbiter, "fibonacciIter");
    measureTime(i, fibbrec, "fibonacciRec");
}

//Roznice w pomiarach miedzy node i Chrome sa nieznaczne
//Jesli chodzi o OpereGx to podobnie nie ma wiekszych roznic w pomiarach