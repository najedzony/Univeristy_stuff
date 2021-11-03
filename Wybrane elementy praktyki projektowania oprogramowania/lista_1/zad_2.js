let ans_pom = 1;
let suma_cyfr = 0;
let kopia = 0;
var ans = [];
for(let i = 1; i <= 100000; i++)
{
    suma_cyfr = 0;
    ans_pom = 1;
    kopia = i;
    while(parseInt(kopia) > 0)
    {
        if(i % (kopia % 10) != 0)
        {
            ans_pom = 0;
        }
        suma_cyfr += kopia % 10;
        kopia = parseInt(kopia / 10);
    }
    if(i % suma_cyfr)
    {
        ans_pom = 0;
    }
    if(ans_pom)
    {
        ans.push(i);
    }
}
console.log(ans);
