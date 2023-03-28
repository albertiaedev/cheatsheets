// Basic syntax

<?php
  // PHP Code
?>
//A PHP file normally contains HTML tags, and some PHP scripting code


//Declaring variables
<?php
  $txt = "Hello world!";  //A variable starts with the $ sign, followed by the name of the variable
  $x = 5;
  $y = 10.5;
?> //Variable names are case-sensitive ($age and $AGE are two different variables)

//Output variables
<?php
  $php = "PHP cheatsheet.";
  echo "I am learning with a $php!";
?> 
//The PHP echo statement is often used to output data to the screen
//Output the sum of two variables
<?php
  $x = 5;
  $y = 4;
  echo $x + $y;
?> 

//Data Types
/*
* PHP supports the following data types:
*   1. String
*   2. Integer
*   3. Float
*   4. Boolean
*   5. Array
*   6. Object
*   7. NULL
*   8. Resource
*/
<?php
  $x = "Hello world"; //STRING
  $x = 1000; //INTEGER
  $x = 1.11; //FLOAT
  $x = true; //or $x = false; //BOOLEAN
  $x = array("one", "two", "three"); //ARRAY
?>

//Constants
<?php
  define("color", "red"; true);
  echo color;
?>

//Built-in functions
<?php

  // For strings
  $var = "This is a string";

  strtolower($var); // Converts the string to lower case
  strtoupper($var); // Converts the string to upper case
  strlen($var); // Tells us how many characters there are in the string
  $var[0]; // Indexing the characters in the string
  $var[0] = "L"; //Replaces the indexed value in the string
  str_replace("string", "phrase", $var); // Replaces a specific word in a string
  substr($var, 8, /*optional, you can tell the number of the last character you want to index*/); // Isolates the string from index 8 and creates a subset with it

  // For numbers
  $num = 100;

  abs($num); // Gives you the absolute value of a number
  pow($num, $num); // Gives you the exponencial number
  sqrt($num); // Gives you the square root of a number
  max($num, $num); // Compares two numbers and tells you the bigger one
  min($num, $num); // Compares two numbers and tells you the smaller one
  round($num); // Rounds the number to its closest integer
  ceil($num); // Rounds the number to its upper integer
  floor($num); // Rounds the number to its lower integer
?>

// Operations with numbers
<?php
  $number = 10;
  // Common operations
  $number++; // Increases the variable $number by a number
  $number--; // Decreases the variable $number by a number
  $number += 10; // This is the equivalent to $number = $number + 10, so the output should be 20
  $number -= 10; // This is the equivalent to $number = $number - 10, so the output should be 0
  $number *= 10; // This is the equivalent to $number = $number * 10, so the output should be 100
  $number /= 10; // This is the equivalent to $number = $number / 10, so the output should be 1
?>

// Getting user input
<?php
  <form action="/*the name of the php page you're working on*/" method="get">
    Input: <input type="text" name="input" placeholder="Your input" />
    <input type="submit" />
  </form>
      
  <br>
      
  <?php echo $_GET["input"] ?>
?>
