/*

Dados los siguientes datos de inversion:
Deposit (cantidad a invertir o guardar)
rate (porcentaje de rendimiento anual)
threshold (cantidad que se desea retirar)

calcular el saldo de la cuanta despues de cada año y como salida proporcionar la cantidad de años en la que dicho salgo igualara o superara el thershold

FUTURE DEVELOPERS

Aaron Merlos

*/

function depositProfit(deposit, rate, threshold){

    let count = 0
    const growthrate = rate * 0.01

    while (deposit < threshold){

        let interest = deposit * growthrate 
        console.log('currently in the account: $' + deposit)
        deposit = deposit + interest
        count += 1

    }
    console.log('currently in the account: $' + deposit)

    return count
}

const result = depositProfit(300, 4, 500)
console.log('\nYou need ' + result + ' years')