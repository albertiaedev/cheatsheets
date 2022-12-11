//TYPESCRIPT CHEATSHEET

//Basic Types
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

//Declarations
let isDone: boolean
let isDone: boolean = false

function add (a: number, b: number): number {
  return a + b
} // Return type is optional
function add (a: number, b: number) { ... }

//Type Assertions
// variables
let len: number = (input as string).length
let len: number = (<string> input).length  /* not allowed in JSX */

// functions
function object(this: {a: number, b: number}, a: number, b: number) {
  this.a = a;
  this.b = b;
  return this;
}

// this is used only for type declaration
let a = object(1,2);
// a has type {a: number, b: number}
                                    
//Interfaces
// inline
function printLabel (options: { label: string }) {
  console.log(options.label)
}
// Note the semicolon
function getUser (): { name: string; age?: number } {
}
                                     
//explicit
interface LabelOptions {
  label: string
}

function printLabel(options: LabelOptions) { ... }

// optional properties
interface User {
  name: string;
  age?: number;
}
                                            
// read only
interface User {
  readonly name: string
}
                                            
// dynamic keys
{
  [key: string]: Object[]
}
                                            
//Type Aliases
type Name = string | string[]
// intersection
interface Colorful { ... }
interface Circle { ... }
type ColorfulCircle = Colorful & Circle;
                                            
//Function Types
interface User { ... }
function getUser(callback: (user: User) => any) { callback({...}) }
getUser(function (user: User) { ... })
