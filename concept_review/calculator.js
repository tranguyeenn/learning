function add(num1, num2) {
    return num1 + num2;
}

function subtract(num1, num2) {
    return num1 - num2;
}

function multiplication(num1, num2) {
    return num1 * num2;
}

function division(num1, num2) {
    return num1/num2;
}

function modulo(num1, num2) {
    return num1 % num2;
}

function exponent(num1, num2) {
    return num1 ** num2;
}

function menu(num1, num2, operator) {
    if (operator === "+") {
        return add(num1, num2);
    }

    else if (operator === "-") {
        return subtract(num1, num2);
    }

    else if (operator === "*") {
        return multiplication(num1, num2);
    }

    else if (operator === "/") {
        return division(num1, num2);
    }

    else if (operator === "%") {
        return modulo(num1, num2);
    }

    else if (operator === "^") {
       return exponent(num1, num2);
    }

    else {
        return "Please enter an appropriate operator";
    }
}

function main() {
    let num1 = prompt("Please enter a number: "); //equivalent of input() in python, automatically a string

    while (num1 != "q" && num1 != "quit") {
        let num2 = prompt("Please enter a number: ");
        let operator = prompt("Enter an operator: ");

        num1 = parseFloat(num1); //equivalent of float() in Python
        num2 = parseFloat(num2);

        console.log(menu(num1, num2, operator))

        num1 = prompt("Please enter a number: ")
    }

    console.log("Bye!")
}

main();