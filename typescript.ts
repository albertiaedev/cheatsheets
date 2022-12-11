//TYPESCRIPT CHEATSHEET

// Basic Types
any
void

boolean
number
string

null
undefined

bigint
symbol

string[]          /* or Array<string> */
[string, number]  /* tuple */

string | null | undefined   /* union */

never  /* unreachable */
unknown

enum Color {
  Red,
  Green,
  Blue = 4
};

let c: Color = Color.Green

// Declarations
let isDone: boolean
let isDone: boolean = false

function add (a: number, b: number): number {
  return a + b
} // Return type is optional
function add (a: number, b: number) { ... }
