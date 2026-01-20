pub fn primitives() {
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
    println!("{}", name);
    name = "Andres Felipe Silva";
    println!("{}", name);

    // Use the variables 'cause the compiler throw a warning
    println!("This is a normal string: {}", string);
    println!("This is a constant: {}", STRING);
}

pub fn strings() {
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

    // Concatenate strings
    let hola: String = String::from("Hola");
    let mundo: String = String::from("Mundo");

    let saludo: String = hola + &mundo;
    println!("{}", saludo);

    // Concat using macro format
    let text: String = format!("Saludo={} Ciudad={}", saludo, city);
    println!("{}", text);
}

pub fn tuples() {
    // To set a tuple we can specify the values into an () simbol, separated by comma
    let tuple: (&str, &str) = ("hola", "mundo");
    println!("Entire simple list: {:?}", tuple); // use :? to format the number

    // Access for elements in specific position use the .index
    println!("First element of tuple: {}", tuple.0);
    // Create a simple vector (list)
    let simple_list: [&str; 1] = ["Hola"];
    println!("Simple list: {:?}", simple_list);

    // We can unextract the content of the tuple using a variable
    let (hola, mundo) = tuple;
    println!("First word={:?} Second word={}", hola, mundo);
}

pub fn slices_and_arrays() {
    // Create a fixed-sizes array
    let fixed_size_array: [i32; 4] = [1, 2, 3, 5];
    println!("{:?}", fixed_size_array);

    // Create an array of strings
    let string_arrays: [String; 2] = [String::from("Hola"), String::from("Mundo")];
    println!("{:?}", string_arrays);

    // Access one element by the index
    println!("{}", string_arrays[1]);

    // Compare two arrays using macro
    let empty_array: [u32; 1] = [3];
    assert!(!empty_array.is_empty());

    let slice: &[u32] = &empty_array;

    let string: String = String::from("Andres");
    let x: &String = &string;
    println!("{:p}", x); // print the reference of the string

    let number: u32 = 5;
    let num: &u32 = &number;
    println!("{:p}", num); // print the reference of the number u32

    assert!(slice.is_empty());
}
