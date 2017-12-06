var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('file2.in')
});
var total = 0;
var nums = [];
lineReader.on('line', function (line) {
    nums.push(parseInt(line));
});
lineReader.on('close', function(){
    var check = true;
    var start = 0; 
    while(check){
        var temp = start;
        start += nums[start];
        if(nums[temp] > 2){
            --nums[temp];
        } else{ 
            ++nums[temp];
        }
        ++total;
        if(start<0 || start>=nums.length){
            check = false;
        }
    }
    console.log(total);
});