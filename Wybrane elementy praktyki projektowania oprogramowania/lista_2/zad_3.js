console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );

//Podzielmy to na 4 części:

(![]+[])[+[]] +  // 1 cześć
// ![] = false                      negacja true
// [] = []               
// ![] + [] = 'false'               dodanie [] powoduje, że dwa argumenty '+' traktowane są jako napisy, i [] to pusty napis
// +[] = 0;                         unarny '+' rzutuje swój argument na Number
// (![] + [])[+[]] = 'false'[0] = 'f'

(![]+[])[+!+[]] +  // 2 część
// ![] + [] = 'false'               wyjaśnione wyżej
// +[] = 0                          wyjaśnione wyżej
// !+[] = true                      negacja wartości numerycznej 0 tworzy wartość true
// +!+[] = 1                        unarny plus rzutuje true na numeryczne 1
// (![] + [])[+!+[]] = 'false'[1] = 'a'
([![]]+[][[]])[+!+[]+[+[]]] + // 3 część
// ![] = false                      wyjaśnione wyżej
// [![]] = [false]                  oczywiste
// [][[]] = undefined               tablica [] nie ma elementy [[]]-tego, więc zwraca się undefined
// [![]]+[][[]] = 'falseundefined'  plus zaaplikowany do tablicy rzutuje dwa argumnenty na napisy (jak wyżej)
// +!+[] = 1                        wyjaśnione wyżej
// [+[]] = [0]                      oczywiste                       
// +!+[]+[+[]] = '10'               dodawanie liczby 1 i tablicy [0] powoduje rzutowanie obu wartości na napisy (jak wyżej)
// ([![]]+[][[]])[+!+[]+[+[]]] = 'falseundefined'[10] = 'i'
(![]+[])[!+[]+!+[]]
// ![]+[] = 'false'                 wyjaśnione wyżej
// !+[] = true                      wyjaśnione wyżej
// !+[] + !+[] = 2                  operator '+' rzutuje obie wartości true na 1 
// (![]+[])[!+[]+!+[]] = 'false'[2] = 'l'

//Ostatecznie 'false'[0] + 'false'[1] + 'falseundefined'[10] + 'false'[2] = 'f' + 'a' + 'i' + 'l' = 'fail'



