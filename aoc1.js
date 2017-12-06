const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('Enter the string:', (toParse) =>{
    size_num = toParse.length;
    var sum_nums = 0;
    for(var x = 0;x<size_num;x++){
        if(x==size_num-1){
            if(toParse.charAt(x) == toParse.charAt(0))
                sum_nums += Number(toParse.charAt(0));
        }
        else{
            if(toParse.charAt(x) == toParse.charAt(x+1))
                sum_nums += Number(toParse.charAt(x+1));
        }
    }
    console.log(sum_nums);
});