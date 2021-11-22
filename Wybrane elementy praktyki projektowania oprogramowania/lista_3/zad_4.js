//Zmienne tworzone za pomocą 'var' wiązane są w obrębie funkcji, co powoduje, że
//w każdym obrocie pętli mamy do czynienia z tym samym 'i'. Funkcje który tworzymy
//w tablicy dostają referencje na tą samą zmienna 'i', która na koniec ma wartość 10.
//Stąd taki wynik działania tego programu

function createFs(n) { // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for ( var i=0; i<n; i++ ) {
        fs[i] = function(i){                        //rozwiązaniem jest związanie zmiennej w ciele funkcji
            return function() {
                return i;
            };
        }(i);
    };
    return fs;
}
var myfs = createFs(10);
console.log( myfs[0]() ); // zerowa funkcja miała zwrócić 0
console.log( myfs[2]() ); // druga miała zwrócić 2
console.log( myfs[7]() );