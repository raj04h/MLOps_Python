f_name="John"
l_name = "Jane"

print(f"Hello {f_name}{l_name}")
print(f"Hello {f_name + l_name}")

int("20")

# Integer
num = 10  

# Float 
dec = 10.5 

# Boolean
is_true = True

# None 
empty = None


# If condition evaluates the Boolean
if is_true:
  print("Condition was true")

# Else catches when if was False  
else: 
  print("Condition was false")

# Try block attempts this code
try:
  result = num / 0
# Except catches the ZeroDivisionError   
except ZeroDivisionError as e:
  print("Cannot divide by 0")



"""
1. loop: A keyword used for an indefinite loop that runs forever until it is broken out of using a break statement or another control flow mechanism.

2. if let: A construct allowing assignment and conditional execution based on the result of an expression, such as checking if an optional value contains a specific type (e.g., an integer).

3. shadowing: The practice of redefining a variable with the same name in the same scope to take on new characteristics or values.

4. type annotations: Explicitly specifying the data type for variables, expressions, and other elements within Rust code to ensure proper compilation and execution.

5. option: A wrapper over an optional value that can contain either a concrete value (e.g., integer) or None.

6. sum: An enum used as a wrapper over an option in the context of this lesson; it provides a convenient way to work with options, especially when combined with pattern matching and if let statements.

7. while loop: A control flow mechanism that continues executing while a specific condition is met.

8. for loop: A control flow mechanism used for iterating over sequences (e.g., ranges or vectors) in Rust.

9. continue: A keyword allowing skipping to the next iteration of a loop when certain conditions are met, such as an odd number in this lesson's example.

10. break: A keyword that allows breaking out of loops and other control flow mechanisms once specific criteria have been satisfied (e.g., finding a seven).
"""


# Loop
"""
let mut x = 0;
loop {
    if x > 5 {
        break;
    }
    println!("{}", x);
    x += 1; // Adding one to reassign the value of `x`.
}
println!("Loop has ended.");
"""

# if let
"""
fn main() {
    let maybe_number = Some(42); // Wrap the integer 42 in a sum (option) enum.
    if let Some(number) = maybe_number { // Use pattern matching to extract the value from the option, if it exists.
        println!("The number is: {}", number);
    } else {
        println!("No number was found.");
    }
}
"""