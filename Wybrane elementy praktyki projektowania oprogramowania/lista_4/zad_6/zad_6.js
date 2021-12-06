var fs = require('fs'),
    readline = require('readline');
const { rawListeners } = require('process');

var rd = readline.createInterface({
    input: fs.createReadStream('./zad_6_pom.txt'),
    output: false,
    console: false
});

dict = {}
var max1 = 0, name1, max2 = 0, name2, max3 = 0, name3;

rd.on('line', function(line) {
    pom = line.slice(9, 20, 0); //wyciągamy adres IP
    if(dict[pom] === undefined)
        dict[pom] = 1;
    else
        dict[pom] += 1;
});

rd.on('close', function(){
    
    for(const i in dict){
        if(dict[i] > max1){
            max1 = dict[i];
            name1 = i;
        }
    }
    for(const i in dict){
        if(dict[i] > max2 && i != name1){
            max2 = dict[i];
            name2 = i;
        }
    }
    for(const i in dict){
        if(dict[i] > max3 && i != name1 && i != name2){
            max3 = dict[i];
            name3 = i;
        }
    }
    console.log(name1 + ' : ' + max1);
    console.log(name2 + ' : ' + max2);
    console.log(name3 + ' : ' + max3);
})

