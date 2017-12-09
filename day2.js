var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('file.in')
});

var sum = 0;
lineReader.on('line', function (line) {
  var array = [];
  var place = '';
  for(var x = 0; x< line.length;x++){
     
      if(line.charAt(x) === '\t'){
            if(place != ''){
                array.push(parseInt(place));
                place = '';
          
            }        
        } 
      else {
          place += line.charAt(x);
      }
   
  }
  if(place != ''){
    array.push(parseInt(place));
    
    }
    array = array.sort(function(a, b){return a-b});
    for(var x = 0; x< array.length-1;x++){
        for(var z = x+1;z < array.length;z++){
            if(array[z]%array[x] == 0){
                sum += array[z]/array[x];
                x = array.length;
                z = array.length;
            }
        }
    }
    
    console.log(sum);
});
