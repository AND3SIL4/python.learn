pub fn primitive_variables() {
    // Declare a normal variables with type notation
    let string: &str = "Andres Felipe Silva";
    println!("Nomal string: {}", string);

    // use let before to reuse the same name of any variable "Shadowing"
    let string: &str = "Felipe Silva";

    // Use the underscore character to indicate to the compiler that the variable is unused
    let _unused_variable: &str = "Variable unused";

    // Declare constants (contants are very inmutable)
    // Constant could be declared using mayus
    // Constants wont inffer the type notation
    const STRING: &str = "This is a constant";

    // To declare mutable variables, use the keyword `mut`
    let mut name: &str = "Andres Silva";
    name = "Andres Felipe Silva";
    println!("{}", name);

    // Use the variables 'cause the compiler throw a warning
    println!("This is a normal string: {}", string);
    println!("This is a constant: {}", STRING);
}

pub fn working_with_strings() {
    // To create string, we can use the following ways
    // 1. .to_string()
    let name: &str = "Andres Felipe Silva";
    let string: String = name.to_string();
    println!("Name: {}", string);

    let hero: String = "Batman".to_string();
    println!("Hero name: {}", hero);

    // 2. Using the string, from method
    let city: String = String::from("Bogota");
    println!("{}", city);
}
