function camelCase(str){
    const array = str.split(" ")
    console.log(array)
    for (i = 0; i < array.length; i++){
        console.log(array[i].charAt(0).toUpperCase() + array[i].slice(1));
    }
}

camelCase("camel case word")

function areaCircle(r){
    console.log(Math.PI * (Math.pow(r,2).toFixed(3)))
    // return Math.PI * Math.pow(r,2).toFixed(3)
}
areaCircle(2)