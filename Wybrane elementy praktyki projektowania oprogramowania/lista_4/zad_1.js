function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
}

Tree.prototype[Symbol.iterator] = function*() {
    arr = [this]
    while(arr.length){
        v = arr.splice(0, 1);
        yield v[0].val;
        if(v[0].left) arr.splice(arr.length - 1, 0, v[0].left);
        if(v[0].right) arr.splice(arr.length - 1, 0, v[0].right);
    }
}

var root = new Tree( 1, new Tree( 2, new Tree( 3 ) ), new Tree( 4 ));


for ( var e of root ) {
    console.log( e );
}
// 1 4 2 3
    