var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('file.in')
});
var total = 0;
lineReader.on('line', function (line) {
  var array = line.split(' ');
  var check = true;
  for(var x = 0;x<array.length;x++){
      for(var z = 0;z<array.length;z++){
          if(z==x){
              
          } else if (array[z].length === array[x].length){
              var count = 0;
              temp1 = array[z];
              temp2 = array[x];
              for(var g = 0;g<temp1.length;g++){
                  for(var t = 0;t<temp1.length;t++){
                      if(temp1.charAt(g)==temp2.charAt(t)){
                          count += 1;
                          temp2 = temp2.slice(0, t) + temp2.slice(t+1);
                          t = temp1.length;
                      }
                  }
              }
              if(count == array[z].length){
                  console.log(array[z]);
                  console.log(array[x]);
                  check = false;
              }
          }
      }
  }
    if(check){
        total += 1;
    }
    console.log(total);
});