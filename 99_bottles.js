function bottleSong(num) {
  // Write your code here! 
  let count = num
  while(count>0){
    console.log(`${count}`+ (count > 1 ? ` bottles` : ` bottle`) + ` of beer on the wall, ${count--}`+ (count > 1 ? ` bottles` : ` bottle`) + ` of beer. \nTake one down and pass it around, ${count}`+ (count > 1 ? ` bottles` : ` bottle`) + ` of beer on the wall.`)
  }

  console.log(`No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, ${num} bottles of beer on the wall.`)

};

let num = 99
bottleSong(num)
