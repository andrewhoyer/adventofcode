
const initial_data = `                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]`;

/*
// Test data
initial_data = `    [D]    
[N] [C]    
[Z] [M] [P]`;
*/

// Set up the core data for the puzzle

const lines = initial_data.split("\n");

let counter = 0;
let stacks = [[],[],[],[],[],[],[],[],[]];
let stacks2 = [[],[],[],[],[],[],[],[],[]];

for (let line of lines) {

	counter = 0
	stack_counter = 0
	
	let single_items = line.split("");
	single_items.shift();
	
	for (let single of single_items) {
		
		if (counter == 0) {
			
			if (single != ' ') {
				stacks[stack_counter].unshift(single);
				stacks2[stack_counter].unshift(single);
			}
			stack_counter++;
		
		}
		
		counter++;
		
		if (counter > 3) {
			counter = 0;
		}
	
	}

}

const instructions = `move 1 from 5 to 2
move 7 from 7 to 1
move 1 from 1 to 7
move 1 from 4 to 1
move 7 from 9 to 1
move 1 from 3 to 7
move 4 from 5 to 4
move 6 from 4 to 9
move 2 from 7 to 6
move 6 from 8 to 2
move 2 from 4 to 5
move 2 from 3 to 7
move 11 from 1 to 4
move 6 from 6 to 1
move 3 from 5 to 3
move 5 from 9 to 8
move 1 from 2 to 3
move 2 from 7 to 9
move 7 from 1 to 2
move 1 from 5 to 3
move 1 from 5 to 3
move 5 from 8 to 5
move 3 from 5 to 4
move 1 from 1 to 7
move 1 from 3 to 8
move 2 from 6 to 3
move 3 from 3 to 4
move 1 from 6 to 2
move 5 from 4 to 2
move 2 from 5 to 3
move 2 from 7 to 1
move 1 from 8 to 1
move 7 from 1 to 7
move 4 from 4 to 2
move 7 from 4 to 1
move 10 from 1 to 5
move 10 from 5 to 2
move 11 from 2 to 3
move 1 from 1 to 6
move 1 from 4 to 7
move 4 from 7 to 1
move 6 from 2 to 5
move 2 from 1 to 3
move 1 from 9 to 5
move 2 from 9 to 6
move 1 from 6 to 1
move 3 from 5 to 4
move 20 from 3 to 9
move 3 from 7 to 1
move 3 from 5 to 2
move 3 from 4 to 8
move 3 from 1 to 3
move 3 from 1 to 2
move 2 from 6 to 1
move 10 from 9 to 6
move 6 from 6 to 7
move 4 from 6 to 3
move 11 from 2 to 6
move 1 from 8 to 9
move 13 from 2 to 3
move 1 from 1 to 9
move 1 from 9 to 4
move 1 from 8 to 2
move 1 from 8 to 2
move 4 from 7 to 8
move 8 from 6 to 9
move 3 from 2 to 3
move 3 from 8 to 4
move 11 from 9 to 2
move 7 from 9 to 6
move 1 from 1 to 5
move 4 from 4 to 9
move 21 from 3 to 1
move 1 from 3 to 9
move 7 from 6 to 3
move 6 from 1 to 2
move 13 from 1 to 5
move 2 from 1 to 2
move 3 from 9 to 3
move 2 from 2 to 3
move 2 from 6 to 4
move 3 from 3 to 5
move 13 from 5 to 2
move 5 from 3 to 4
move 2 from 7 to 9
move 2 from 4 to 2
move 1 from 3 to 8
move 1 from 6 to 1
move 4 from 3 to 7
move 2 from 5 to 7
move 1 from 7 to 2
move 1 from 5 to 9
move 4 from 7 to 8
move 1 from 1 to 9
move 6 from 8 to 1
move 4 from 4 to 8
move 25 from 2 to 9
move 1 from 4 to 3
move 1 from 3 to 7
move 4 from 8 to 1
move 1 from 7 to 4
move 3 from 1 to 6
move 5 from 2 to 1
move 1 from 5 to 1
move 1 from 4 to 1
move 24 from 9 to 6
move 9 from 1 to 6
move 1 from 5 to 6
move 1 from 1 to 9
move 1 from 2 to 8
move 1 from 8 to 1
move 3 from 1 to 8
move 36 from 6 to 3
move 2 from 7 to 3
move 1 from 2 to 5
move 1 from 5 to 2
move 1 from 6 to 2
move 10 from 3 to 2
move 3 from 8 to 2
move 1 from 1 to 7
move 2 from 2 to 6
move 10 from 9 to 1
move 2 from 6 to 4
move 13 from 3 to 4
move 8 from 3 to 7
move 8 from 1 to 2
move 5 from 3 to 8
move 3 from 1 to 9
move 1 from 7 to 1
move 7 from 4 to 5
move 1 from 1 to 2
move 14 from 2 to 6
move 2 from 7 to 2
move 8 from 4 to 8
move 3 from 7 to 9
move 2 from 9 to 8
move 2 from 7 to 1
move 1 from 7 to 8
move 1 from 6 to 8
move 1 from 9 to 3
move 4 from 2 to 7
move 6 from 6 to 1
move 3 from 1 to 9
move 1 from 1 to 7
move 6 from 5 to 6
move 1 from 5 to 2
move 1 from 6 to 8
move 5 from 7 to 5
move 1 from 2 to 9
move 2 from 3 to 4
move 9 from 8 to 4
move 8 from 4 to 8
move 6 from 6 to 7
move 5 from 6 to 4
move 7 from 9 to 7
move 7 from 8 to 7
move 5 from 8 to 4
move 3 from 1 to 6
move 1 from 2 to 7
move 1 from 1 to 4
move 4 from 5 to 2
move 2 from 6 to 9
move 1 from 3 to 7
move 1 from 5 to 1
move 1 from 8 to 9
move 1 from 6 to 1
move 1 from 2 to 7
move 2 from 8 to 1
move 2 from 1 to 8
move 3 from 2 to 4
move 1 from 6 to 1
move 17 from 4 to 1
move 3 from 2 to 7
move 13 from 7 to 8
move 1 from 2 to 6
move 14 from 1 to 4
move 2 from 8 to 5
move 1 from 9 to 7
move 2 from 5 to 4
move 1 from 9 to 3
move 5 from 1 to 5
move 3 from 4 to 1
move 1 from 3 to 2
move 7 from 4 to 5
move 9 from 7 to 8
move 5 from 4 to 2
move 1 from 1 to 3
move 1 from 9 to 2
move 15 from 8 to 6
move 1 from 3 to 7
move 11 from 6 to 5
move 1 from 4 to 8
move 3 from 1 to 7
move 5 from 7 to 5
move 27 from 5 to 1
move 8 from 8 to 4
move 1 from 2 to 6
move 3 from 6 to 1
move 9 from 1 to 5
move 5 from 5 to 7
move 2 from 2 to 1
move 2 from 5 to 4
move 6 from 7 to 6
move 1 from 5 to 2
move 1 from 7 to 8
move 4 from 6 to 8
move 5 from 6 to 3
move 1 from 7 to 1
move 5 from 4 to 3
move 6 from 8 to 2
move 1 from 7 to 8
move 2 from 8 to 9
move 10 from 3 to 5
move 9 from 5 to 2
move 3 from 4 to 8
move 1 from 5 to 7
move 2 from 9 to 7
move 2 from 8 to 3
move 1 from 3 to 8
move 19 from 1 to 7
move 4 from 2 to 7
move 2 from 4 to 3
move 3 from 3 to 2
move 2 from 8 to 3
move 2 from 5 to 8
move 1 from 2 to 3
move 2 from 8 to 3
move 5 from 2 to 5
move 9 from 7 to 5
move 13 from 5 to 9
move 7 from 2 to 6
move 2 from 6 to 9
move 1 from 2 to 1
move 5 from 6 to 7
move 1 from 5 to 7
move 6 from 1 to 2
move 5 from 3 to 6
move 6 from 7 to 2
move 3 from 6 to 4
move 3 from 7 to 4
move 12 from 7 to 6
move 5 from 4 to 1
move 2 from 7 to 4
move 3 from 4 to 6
move 16 from 6 to 3
move 4 from 1 to 4
move 1 from 1 to 9
move 3 from 9 to 2
move 1 from 4 to 6
move 9 from 3 to 7
move 2 from 6 to 3
move 3 from 3 to 9
move 15 from 2 to 7
move 19 from 7 to 4
move 15 from 9 to 2
move 16 from 2 to 8
move 6 from 3 to 5
move 4 from 7 to 5
move 15 from 8 to 7
move 19 from 4 to 2
move 1 from 8 to 3
move 16 from 2 to 1
move 9 from 7 to 6
move 7 from 2 to 8
move 2 from 2 to 7
move 1 from 9 to 5
move 1 from 3 to 4
move 6 from 1 to 2
move 8 from 5 to 1
move 1 from 5 to 1
move 18 from 1 to 8
move 7 from 7 to 5
move 7 from 5 to 3
move 4 from 3 to 6
move 13 from 8 to 5
move 12 from 8 to 1
move 5 from 1 to 6
move 15 from 5 to 4
move 1 from 1 to 6
move 12 from 6 to 3
move 8 from 3 to 4
move 2 from 7 to 3
move 9 from 3 to 1
move 5 from 2 to 9
move 16 from 4 to 3
move 10 from 1 to 3
move 2 from 1 to 5
move 1 from 3 to 1
move 5 from 6 to 1
move 4 from 9 to 3
move 1 from 2 to 8
move 1 from 8 to 1
move 1 from 9 to 8
move 2 from 5 to 9
move 9 from 4 to 1
move 3 from 1 to 3
move 2 from 6 to 8
move 3 from 8 to 5
move 2 from 1 to 5
move 2 from 9 to 8
move 1 from 8 to 6
move 2 from 5 to 3
move 19 from 3 to 1
move 2 from 4 to 2
move 1 from 5 to 6
move 2 from 2 to 3
move 1 from 8 to 6
move 8 from 3 to 9
move 6 from 3 to 7
move 2 from 6 to 2
move 1 from 6 to 1
move 1 from 1 to 8
move 1 from 8 to 9
move 1 from 7 to 3
move 19 from 1 to 5
move 21 from 5 to 2
move 13 from 2 to 6
move 13 from 1 to 8
move 7 from 9 to 7
move 2 from 9 to 2
move 10 from 8 to 3
move 1 from 1 to 6
move 10 from 2 to 4
move 11 from 3 to 5
move 8 from 5 to 6
move 1 from 3 to 7
move 2 from 8 to 6
move 2 from 2 to 8
move 3 from 7 to 6
move 2 from 8 to 6
move 1 from 1 to 2
move 24 from 6 to 5
move 2 from 3 to 8
move 1 from 8 to 6
move 7 from 7 to 9
move 4 from 6 to 9
move 1 from 8 to 9
move 21 from 5 to 9
move 2 from 7 to 2
move 1 from 8 to 5
move 1 from 7 to 3
move 12 from 9 to 6
move 6 from 6 to 3
move 12 from 9 to 4
move 4 from 5 to 6
move 13 from 4 to 2
move 8 from 4 to 8
move 10 from 6 to 8
move 11 from 8 to 9
move 4 from 8 to 4
move 2 from 4 to 3
move 8 from 3 to 8
move 2 from 6 to 8
move 1 from 3 to 8
move 6 from 2 to 4
move 1 from 4 to 8
move 1 from 9 to 7
move 13 from 8 to 4
move 1 from 7 to 1
move 1 from 1 to 4
move 8 from 4 to 7
move 3 from 5 to 7
move 19 from 9 to 7
move 3 from 2 to 7
move 1 from 8 to 2
move 13 from 7 to 6
move 1 from 2 to 4
move 4 from 6 to 2
move 1 from 8 to 3
move 7 from 6 to 8
move 1 from 6 to 2
move 1 from 2 to 7
move 9 from 2 to 3
move 1 from 6 to 2
move 21 from 7 to 5
move 9 from 5 to 3
move 19 from 3 to 9
move 5 from 8 to 5
move 2 from 2 to 1
move 2 from 1 to 8
move 6 from 4 to 5
move 3 from 8 to 7
move 15 from 9 to 2
move 2 from 2 to 5
move 3 from 9 to 6
move 5 from 4 to 5
move 11 from 2 to 6
move 1 from 8 to 6
move 1 from 9 to 5
move 1 from 7 to 3
move 6 from 5 to 6
move 1 from 4 to 6
move 1 from 3 to 4
move 13 from 5 to 2
move 16 from 6 to 9
move 4 from 4 to 5
move 2 from 6 to 2
move 2 from 6 to 4
move 2 from 4 to 5
move 2 from 7 to 8
move 2 from 6 to 3
move 2 from 5 to 8
move 14 from 5 to 7
move 4 from 8 to 1
move 4 from 1 to 6
move 1 from 3 to 9
move 1 from 6 to 1
move 2 from 7 to 3
move 2 from 3 to 7
move 2 from 5 to 2
move 9 from 9 to 2
move 13 from 7 to 3
move 12 from 3 to 9
move 2 from 6 to 8
move 14 from 2 to 9
move 2 from 8 to 9
move 10 from 2 to 1
move 1 from 7 to 4
move 2 from 3 to 8
move 4 from 2 to 1
move 1 from 8 to 3
move 1 from 2 to 6
move 1 from 8 to 3
move 4 from 9 to 4
move 1 from 3 to 5
move 1 from 5 to 1
move 1 from 3 to 9
move 12 from 1 to 8
move 10 from 8 to 5
move 7 from 5 to 6
move 1 from 1 to 9
move 3 from 5 to 1
move 1 from 1 to 3
move 16 from 9 to 7
move 4 from 4 to 3
move 1 from 4 to 9
move 15 from 7 to 8
move 15 from 9 to 1
move 8 from 1 to 6
move 1 from 9 to 3
move 17 from 6 to 2
move 1 from 9 to 1
move 15 from 2 to 7
move 14 from 8 to 9
move 12 from 7 to 9
move 12 from 9 to 3
move 3 from 7 to 9
move 1 from 7 to 4
move 7 from 9 to 6
move 1 from 4 to 6
move 11 from 9 to 6
move 2 from 1 to 2
move 18 from 6 to 4
move 4 from 2 to 7
move 2 from 7 to 3
move 2 from 7 to 8
move 4 from 1 to 5
move 1 from 9 to 2
move 2 from 5 to 4
move 5 from 1 to 3
move 2 from 3 to 7
move 2 from 3 to 9
move 1 from 6 to 7
move 1 from 2 to 9
move 2 from 8 to 1
move 3 from 1 to 3
move 2 from 5 to 8
move 2 from 3 to 5
move 1 from 5 to 2
move 1 from 1 to 3
move 1 from 9 to 2
move 1 from 9 to 1
move 3 from 7 to 6
move 1 from 1 to 9
move 2 from 8 to 9
move 1 from 2 to 3
move 2 from 8 to 2
move 2 from 6 to 5
move 1 from 8 to 5
move 3 from 2 to 5
move 3 from 4 to 8
move 1 from 8 to 2
move 3 from 9 to 7
move 3 from 7 to 1
move 1 from 9 to 6
move 3 from 1 to 2
move 2 from 8 to 7
move 2 from 7 to 9
move 2 from 6 to 5
move 3 from 5 to 3
move 1 from 2 to 5
move 3 from 2 to 7
move 2 from 5 to 6
move 15 from 4 to 9
move 1 from 3 to 1
move 25 from 3 to 4
move 3 from 7 to 3
move 5 from 9 to 5
move 10 from 9 to 5
move 9 from 5 to 1
move 5 from 5 to 2
move 1 from 6 to 7
move 5 from 5 to 8
`;


/*
// Test instructions
instructions = `move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`;
*/


// Trigger calculations when the page loads

$(document).ready(function() {

	part1();
	part2();

	update_display();


});

// Part 1 solution
function part1() {
	for (const instruction of instructions.split("\n")) {

		let instr_part = instruction.split(" ");

		for (let i = 1; i <= parseInt(instr_part[1]); i++) {

				let box = stacks[parseInt(instr_part[3]) - 1].pop();
				stacks[parseInt(instr_part[5]) - 1].push(box);

		}	

	}

	let phrase = "";

	for (const stack of stacks) {
		phrase += stack[stack.length - 1];
	}

	console.log("Part 1: " + phrase);		
	
}

// Part 2 solution
function part2() {
	for (const instruction of instructions.split("\n")) {

		const instr_part = instruction.split(" ");

		let move_array = [];
		for (let i = 1; i <= parseInt(instr_part[1]); i++) {
			
			move_array.unshift(stacks2[parseInt(instr_part[3]) - 1].pop());

		}	

		for (const box of move_array) {
			stacks2[parseInt(instr_part[5]) - 1].push(box);
		}

	}

	let phrase = "";

	for (const stack of stacks2) {
		phrase += stack[stack.length - 1];
	}

	console.log("Part 2: " + phrase);		
	
}

// Display the resulting stacks on the page
function update_display() {
	
	// Part 1
	let counter = 0;

	for (const stack of stacks) {

		let pile = (counter + 1) + ": ";
		for (const box of stack) {
			pile = pile + box;
		}
	
		$('#row' + counter).html(pile)
		counter++;

	} 
	
	// Part 2
	counter = 0;

	for (const stack of stacks2) {

		let pile = (counter + 1) + ": ";
		for (const box of stack) {
			pile = pile + box;
		}
	
		$('#row' + counter + "-2").html(pile)
		counter++;

	} 		
}
