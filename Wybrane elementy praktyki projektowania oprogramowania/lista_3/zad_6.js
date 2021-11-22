function createGenerator(n) {
    return function () {
        var _state = 0;
        return {
            next: function () {
                return {
                    value: _state,
                    done:  _state++ >= n
                }
            }
        }
    }
}

var foo1 = {
    [Symbol.iterator]: createGenerator(1)
};

var foo2 = {
    [Symbol.iterator]: createGenerator(2)
}

var foo3 = {
    [Symbol.iterator]: createGenerator(3)
}

console.log("------")
for (var x of foo1) {
    console.log(x);
}

console.log("-----")
for (var x of foo2) {
    console.log(x);
}

console.log("-----")
for (var x of foo3) {
    console.log(x);
}