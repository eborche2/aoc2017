var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('file3.in')
});
var total = 0;
var nums = [];
lineReader.on('line', function (line) {
    nums = line.split('\t', ).map(Number);
});
lineReader.on('close', function(){
   var iterations = [];
   var check = true;
    while(check){
        iterations.push(nums.toString());
        var max = Math.max.apply(null, nums);
        var i = nums.indexOf(max);
        nums[i] = 0;
        i++;
        for(var x = 0;x<max;x++){
            if(i==16){
                i = 0;
            }
            ++nums[i++];
        }
        ++total;
        for(var x = 0;x<iterations.length;x++){
            if(iterations[x]==nums.toString()){
                check = false;
                console.log(total-x);//part 2
            }
        }
    }
    console.log(total);//part 1
});