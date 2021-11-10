function levenshteinDistance (a, b){


    //crear matriz base null
    const distanceMatrix = Array(a.length + 1).fill(null).
        map(() => Array(b.length + 1).fill(null))


    //llenar primer fila
    for (let i = 0; i <= b.length; i += 1){
        distanceMatrix[0][i] = i
    }

    //llenar primer columna
    for (let j = 0; j <= a.length; j += 1){
        distanceMatrix[j][0] = j
    }

    //calcular distancias 
    for (let i = 1; i <= a.length; i += 1){
        for (let j = 1; j <= b.length; j += 1){
            const indicator = a[i - 1] === b[j - 1] ? 0 : 1

            distanceMatrix[i][j] = Math.min(    
                distanceMatrix[i][j-1] + 1, //insertar letra
                distanceMatrix[i-1][j] + 1, //borrar letra
                distanceMatrix[i-1][j-1] + indicator, // reemplazar o no hacer nada
            )
        }
    }

     //devolver el valor de distancia
     console.log("\n\t***MATRIZ***\n")
     console.log(distanceMatrix)

    return distanceMatrix[a.length][b.length]
}

const result = levenshteinDistance('casas', 'cosa')
console.log("\nEl numero de movimientos para realizar su transformacion (distancia) es: " + result)