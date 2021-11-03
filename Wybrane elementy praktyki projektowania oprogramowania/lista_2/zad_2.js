/*
1. Użycie operatorów . oraz [] do odwoływania się do składowych obiektu.
*/

let obiekt = {};

obiekt.a = 1;
console.log(obiekt['a']);

obiekt['b'] = 2;
console.log(obiekt.b);

// Jakie możemy znaleźć różnice między tymi dwoma sposobami?
// Operator [] pozwala na użycie dowolnych napisów jako kluczy, np:

obiekt['a 1 * = '] = 3
console.log(obiekt['a 1 * = '])

//natomiast nie da się console.log(a.a 1 * =)

/*
2. Użycie argumentów innego typu niż string dla operatora [] dostępy do składowej obiektu.
*/

//Co się dzieje jeśli argumentem jest liczba?

let obiekt1 = {};
obiekt1[1] = 1;
console.log(obiekt1);

//Zostaje zamieniona na napis.

//Co się dzieje jeśli argumentem operatora jest inny obiekt?

obiekt1[obiekt] = 2;
console.log(obiekt1);

//Obiekt zostaje zamieniony na napis.

//Jaki wpływ na klucz pod jakim zostanie zapisana wartość ma programista w obu przypadkach?
//W przypadku obiektów klucz zależy od metody toString, którą programista może przeciążyć własną funkcją.
//W przypadku liczb programista jest zdany na wbudowaną konwersję wartości numerycznych na napisy.

/*
3. Użycie argumentów innego typu niż number dla operatora [] dostępu do tablicy.
*/

//Co jeśli argumentem operatora jest napis?

let tab = [1, 3, 3, 7];
console.log(tab['1']); 

//Napis rzutowany jest na liczbę jeżeli jest to możliwe.

tab['a'] = 'b'; //klucz jest dodawany jak do zwykłego obiektu
console.log(tab);

//Co się dzieje, jeśli argumentem operatora jest inny obiekt?

tab[{}] = {};
console.log(tab); //zachowanie obiektów jako kluczy jest identyczne jak w przypadku obiektów

tab[new Number(0)] = 997;
console.log(tab); //Number traktowany jest jako wartość numeryczna

//Czy i jak zmienia się zawartość tablicy jeśli zostanie od niej dopisana właściwość pod kluczem, który nie jest liczbą?
//Tak jak wyżej, do tablicy dodawane są nowe atrybuty.

//Czy można ustawiać wartość atrybutu length tablicy na inną wartość niż liczba elementów w tablicy? Co się dzieje, jeśli ustawia się wartość mniejszą niż liczba elementów,
//a co jeśli ustawia się wartość większą niż liczba elementów?

tab.length = 1;
console.log(tab); // Dalsze elementy zostały ucięte

tab.length = 10;
console.log(tab); //Tablica została rozszerzona o "puste elementy"
console.log(tab[2]); //undefined
