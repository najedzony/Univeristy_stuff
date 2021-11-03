/*
    Operator 'instanceof' pozwala sprawdzić, czy dana wartość jest instancją
    pewnego typu (konstruktora), jednak nie działa na typy proste.
    Zwraca wartość boolowską.
*/

console.log(new String("zadanie4") instanceof String);
console.log("zadanie4" instanceof String);

/*
    Operator 'typeof' pozwala na uzyskanie typu danego wyrażenia. Zwraca
    napis, który reprezentuje dany typ. Zwracany napis zwraca nazwę typu
    dla typów prostych lub 'object' dla wszystkich złożonych.
*/

console.log(typeof 911);
console.log(typeof (new Number(911)));

console.log(typeof "zadanie4");
console.log(typeof (new String("zadanie4")));
