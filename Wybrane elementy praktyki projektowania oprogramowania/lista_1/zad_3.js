function isPrime(num)
{
    for(let i = 2; i * i <= num; i++)
    {
        if(num % i == 0)
        {
            return false;
        }
    }
    return true;
}

var ans = [];

for(let i = 2; i <= 100000; i++)
{
    if(isPrime(i))
    {
        ans.push(i);
    }
}

console.log(ans);
