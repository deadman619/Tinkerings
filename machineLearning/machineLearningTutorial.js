const brain = require('brain.js');
const data = require('./data.json');
// const network = new brain.NeuralNetwork();

// network.train([
// 	{ input: [0,0,0], output: [0] },
// 	{ input: [0,0,1], output: [0] },
// 	{ input: [0,1,1], output: [0] },
// 	{ input: [1,0,1], output: [1] },
// 	{ input: [1,1,1], output: [1] },
// ]);

// network.train([                    // Train to recognize which team is more likely to win
// 	{ input: [1,2], output: [1] }, // Team 2 wins
// 	{ input: [1,3], output: [1] }, // Team 3 wins
// 	{ input: [2,3], output: [0] }, // Team 2 wins
// 	{ input: [2,4], output: [1] }, // Team 4 wins
// 	{ input: [1,2], output: [0] }, // Team 1 wins
// 	{ input: [1,3], output: [0] }, // Team 1 wins
// 	{ input: [3,4], output: [0] }  // Team 3 wins 
// ]);

// const output = network.run([1,4]); // Closer to 0 means team 1 favored, closer to 1 means team 4 favored

// console.log(`Prob: ${output}`);

const network = new brain.recurrent.LSTM();

const trainingData = data.map(item => ({   
	input: item.text,
	output: item.category
}));

network.train(trainingData, {     // Go through the data x amount of times to learn more accurately
	iterations: 200
});

const output = network.run('Woooooooooow bugged game mechanics dude');

console.log(`Category: ${output}`);