// 1. Inicjalizacja
// 1.1 dane wejściowe:
// - target sentence
// - ilość próbek
// - współczynnik mutacji
// 1.2 wygeneruj N randomowych zdań z charsetu
// 2. Fitness function
// 2.1 oblicz wartość punktową fitness dla każdego zdania
// 3. Selekcja
// 3.1 na podstawie fitness function znajdź rodziców (?)
// 3.2 Crossover - wygeneruj dziecko na podstawie genów rodziców
// 3.3 Mutation - wprowadź losowosć w genach dziecka
// 2. Fitness function
// ...


const target = "to be or not to be";
const variationNumber = 200;
const mutationRate = 0.01;

// 1.

function randomSentence() {
    var sentence = "";
    for (var i = 0; i < target.length; i++) {
        sentence += randomChar();
    }
    return sentence;
}

function randomChar() {
    var characters = 'abcdefghijklmnopqrstuvwxyz ';
    return characters.charAt(Math.floor(Math.random() * characters.length))
}

var sequence = [];
for (var i = 0; i < variationNumber; i++) {
    sequence.push(randomSentence());
}
for (var i = 0; i < sequence.length; i++) {
    console.log(`${i}. ${sequence[i]}`);
}