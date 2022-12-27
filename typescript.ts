//TYPESCRIPT CHEATSHEET

//Basic Types

// any (for unknown data types)
let someVariable: any = 10;
let someVariable: any = 'string';
let someVariable: any = true;

// void (declaration for functions that do not return a value)
function funcVoid(message: string): void {
    console.log(message);
}

// boolean
let bool: boolean = true;
let bool: boolean = false;

//number
let num: number = 10;

// string
let str: string = "I'm learning TypeScript";


null
undefined

bigint
symbol

// array
string[]          /* or Array<string> */
[string, number]  /* tuple */

string | null | undefined   /* union */

never  /* unreachable */
unknown

// enum
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

//Classes
class Point {
  x: number
  y: number
  static instances = 0
  constructor(x: number, y: number) {
    this.x = x
    this.y = y
  }
}
// inheritance
class Point {...}
class Point3D extends Point {...}
interface Colored {...}
class Pixel extends Point implements Colored {...}

// short fields initialization
class Point {
  static instances = 0;
  constructor(
    public x: number,
    public y: number,
  ){}
}
                               
// fields which do not require initialization
class Point {
  public someUselessValue!: number;
  ...
}

//Generics
class Greeter<T> {
  greeting: T
  constructor(message: T) {
    this.greeting = message
  }
}
let greeter = new Greeter<string>('Hello, world')

//Modules
export interface User { ... }

//Type extraction
interface Building {
  room: {
    door: string;
    walls: string[];
  };
}
type Walls = Building['room']['walls']; // string[]

//Keyof Type Operator
type Point = { x: number; y: number };
type P = keyof Point; // x | y

//Conditional Types
// someType extends otherType ? TrueType : FalseType;
type ToArray<T> = T extends any ? T[] : never;
type StrArrOrNumArr = ToArray<string | number>; // string[] | number[]
// inferring
type GetReturnType<T> = T extends (...args: unknown[]) => infer R
  ? R
  : never;
type Num = GetReturnType<() => number>; // number
type First<T extends Array<any>> = T extends [infer F, ...infer Rest] ? F : never;
type Str = First<['hello', 1, false]>; // 'hello'

//Literal Type
const point = { x: 4, y: 2 }; // { x: number, y: number }
const literalPoint = { x: 4, y: 2 } as const; // { readonly x: 4, readonly y: 2 };

//Template Literal Type
type SpaceChar = ' ' | '\n' | '\t';
type TrimLeft<S extends string> = S extends `${SpaceChar}${infer Rest}` ? TrimLeft<Rest> : S;
type Str = TrimLeft<'    hello'>; // 'hello'

//Classes
class Calculator {
    private result: number;
    
    constructor(){
        this.result = 0;
    }
    
    add(x: number) {
        this.result += x;
    }
    
    substract(x: number) {
        this.result -= x;
    }
    
    getResult(): number {
        return.this.result;
    }
}
