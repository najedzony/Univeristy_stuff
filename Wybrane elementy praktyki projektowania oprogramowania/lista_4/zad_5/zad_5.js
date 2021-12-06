var fs = require('fs');

fs.readFile('pom.txt', 'utf-8', (err, data) =>{
    console.log(data);
});