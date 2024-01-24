
let numeros = [1,2,3,4,5]

// a funcao reduce ira somar todos os elementos do array resultando apenas 1 unico valor

let somatotal1 = numeros.reduce(reduce(function(x,y){
    return x+y
}));

console.log("soma dos elementos")