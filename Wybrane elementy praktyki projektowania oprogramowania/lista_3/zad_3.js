function forEach(a, f){
    for(var x of a){
        f(x);
    }
}

function map(a, f){
    var tab = [];
    for(var x of a){
        tab.push(f(x));
    }
    return tab;
}

function filter(a, f){
    var tab = []
    for(var x of a){
        if(f(x)){
            tab.push(x);
        }
    }
    return tab;
}

var a = [1,2,3,4];

forEach( a, _ => { console.log( _ ); } );
// [1,2,3,4]
console.log(filter( a, _ => _ < 3 ));
// [1,2]
console.log(map( a, _ => _ * 2 ));
// [2,4,6,8]