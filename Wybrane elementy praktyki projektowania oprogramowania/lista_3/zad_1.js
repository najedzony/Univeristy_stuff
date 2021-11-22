var object = {
    x : 0,

    get func(){
        return object.x;
    },

    set func(x){
        object.x = x; 
    },

    wypisywanie : function(){
        console.log(object.x);
    }
}

object.func = 10;

// Nowe pola do obiektu można dodawać używając [], . lub Object.defineProperty

object['n'] = 20

object.nowaMetoda = function(){
    return object['x'] * object['n'];
}

console.log(object.nowaMetoda());

// Natomiast nowe właściowości get/set można dodawać jedynie za pomocą Object.defineProperty

Object.defineProperty(object, 'nowaFunkcja', {
    get : function(){
        return object.x;
    },

    set : function(x){
        object.x = x;
    }
})

object.nowaFunkcja = 100;
console.log(object.nowaFunkcja);