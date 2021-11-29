/*

Imprimir la cadena o cadenas mas largas de una lista o arreglo proporcionado
de igual manera imprimir la cantidad de caracteres de la cadena mas larga

FUTURE DEVELOPERS

Aaron Merlos

*/


function allLongestStrings(inputArray){

    let longestSize = -1
    const result = []

    for (let i = 0; i < inputArray.length; i+=1){

        if (inputArray[i].length > longestSize){

            longestSize = inputArray[i].length
            
        }

    }

    for (let i = 0; i < inputArray.length; i += 1){

        if (inputArray[i].length === longestSize){

            result.push(inputArray[i])

        }

    }

    console.log('\nLa cantidad de caracteres de la cadena mas larga es: ' + longestSize + '\nLa(s) cadena(s) mas larga(s) es/son: ')

    return result
}


const inputArray = ["aba", "erty", "aa", "poiu", "ad", "vcd", "aba"]
const result = allLongestStrings(inputArray)
console.log(result)

