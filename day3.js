const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
/**
rl.question('Please enter location:', (loc)=>{
    var start = parseInt(loc);
    var theroot = parseInt(Math.sqrt(start))
    if(theroot%2 == 0){
        theroot += 1;
    } else{
        theroot += 2;
    }
    console.log(theroot);
    var point = start - ((theroot-2) * (theroot-2));
    var half = parseInt(theroot/2);
    console.log(point);
    if(point == 0){
        console.log(theroot-3);
    }
    else if(point%half == 0){
        var check = point/half;
        if(check%2 ==0){
            console.log(theroot -1);
        }
        else {
            console.log(half);
        }
    } else{
        var toadd = point%half;
        console.log(half + toadd);
    }
});
**/
    var inner = [1, 2, 4, 5, 10, 11, 23, 25];
    
    var row = 1;
    
    var enough = true;
while(enough){
    var next = [];
    var theroot = 3 + (row * 2);
    var half = parseInt(theroot/2);
    var after = false;
    var first = true;
    var corner = 0;
    console.log(half);
    for(var x = 1; x<= (1 + row)*8;x++){
        console.log(x);
        if(x == 1){
            next.push(inner[0] + inner[inner.length-1]);
        } else if(x%half == 0){
            var check = parseInt(x/half);
          
            if(check%2 == 1){
                console.log("middle");
                var sum = next[next.length-1];
                first = false;
              
                sum += inner[x-(2* (check/2))];
       
                sum += inner[x-(2 * (check/2)) - 1];
               
                if(x-3 < 0){
                    sum += inner[inner.length-1];
                }
                else {
                    sum += inner[x-(2 * (check/2)) - 2];
                }
             
                next.push(sum);
            } else {
                console.log("corner");
                var sum = next[next.length-1];
          
                sum += inner[x - (check) - 1]
                if(corner == 4){
                    sum += next[0];
                }
                next.push(sum);
            }
        } else if((parseInt((x+1)/half)%2 == 0|| parseInt((x-1)/half)%2 == 0) && first != true){
            var check = parseInt(x/half);
            
            if(after != true){
                console.log("corener before");
            
                var sum = inner[x - (2*(check/2))-1];
            
                sum += next[next.length-1];
                
                sum += inner[x-(2*(check/2))-2];
                corner += 1
                if(corner == 4){
                    sum += next[0];
                }
                next.push(sum);
                after = true;
                
            } else {
                console.log("corener after");
                var sum = next[next.length-2];
                sum += next[next.length-1];
                sum += inner[x-(2*(check/2))-1];
                sum += inner[x-(2*(check/2))-2];
                next.push(sum);
                after = false;
                first = true;
                
            }
        } else {
            if(first != true){ 
                var check = parseInt(x/half);
                    console.log("regular");
                    var sum = next[next.length-1];
                    console.log(sum);
                    console.log(x-(2*(check/2)));
                    sum += inner[x-(2* (check/2))];
                console.log(sum);
                    sum += inner[x-(2 * (check/2)) - 1];
                console.log(sum);
                    if(x-2 < 0){
                        sum += inner[inner.length-1];
                    }
                    else {
                        sum += inner[x-(2 * (check/2)) - 2];
                    }
                console.log(sum);
                    next.push(sum);
            } else {
                var check = parseInt(x/half);
                    console.log("regular");
                    var sum = next[next.length-1];
                    console.log(sum);
                    console.log(x-(2*(check/2)));
                    sum += inner[x-(2* (check/2)) - 1];
                console.log(sum);
                    sum += inner[x-(2 * (check/2)) - 2];
                console.log(sum);
                    if(x-3 < 0){
                        sum += inner[inner.length-1];
                    }
                    else {
                        sum += inner[x-(2 * (check/2)) - 3];
                    }
                console.log(sum);
                    next.push(sum);
            }
        
        
    }
    }
   
    if(next[next.length-1] > 361527){
        enough = false;
        console.log(next);
    } else {
        inner = next;
        row += 1;
        console.log(next);
        first = true;
    }

  
}
    
