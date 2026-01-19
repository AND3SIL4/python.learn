# AGENTS.md

This file contains guidelines and commands for agentic coding agents working in this Rust repository.

## Repository Overview

This is a Rust learning repository containing basic exercises and examples. The repository is organized into:
- `src/main.rs` - Main entry point
- `src/basics/` - Basic Rust concepts and exercises
- `src/basics/variables.rs` - Variable examples
- `src/basics/flow_controls.rs` - Control flow examples

## Development Commands

### Build and Run
```bash
# Build the project
cargo build

# Build and run
cargo run

# Build for release
cargo build --release
```

### Code Quality
```bash
# Check code without building
cargo check

# Lint with Clippy
cargo clippy

# Format code with rustfmt
cargo fmt

# Format check (without modifying files)
cargo fmt --check
```

### Testing
```bash
# Run all tests
cargo test

# Run specific test
cargo test [test_name]

# Run tests in specific file
cargo test --bin [binary_name]

# Run tests with output
cargo test -- --nocapture

# Run single test with verbose output
cargo test -- --exact --nocapture
```

### Documentation
```bash
# Generate and open documentation
cargo doc --open

# Check documentation coverage
cargo doc --document-private-items
```

## Code Style Guidelines

### General Principles
- Follow Rust idioms and conventions
- Use `rustfmt` for consistent formatting
- Prefer explicit types over inference when clarity is needed
- Use meaningful variable and function names
- Keep functions focused and small

### Import Organization
```rust
// Standard library imports
use std::collections::HashMap;
use std::fs::File;
use std::io::Read;

// External crate imports
use serde::{Deserialize, Serialize};
use tokio::runtime::Runtime;

// Local module imports
use crate::basics::variables;
use super::flow_controls;
```

### Type Annotations
```rust
// Function signatures with explicit types
fn process_data(data: &Vec<String>) -> Result<HashMap<String, i32>, Error> {
    // Implementation
}

// Variable annotations when inference isn't clear
let items: Vec<String> = Vec::new();
let result: Result<i32, Error> = parse_input(input);
```

### Function Documentation
```rust
/// Calculate the factorial of a given number recursively.
///
/// # Arguments
/// 
/// * `number` - A non-negative integer
///
/// # Returns
///
/// The factorial of the input number
///
/// # Examples
///
/// ```
/// let result = factorial(5);
/// assert_eq!(result, 120);
/// ```
///
/// # Panics
///
/// Panics if input is negative
fn factorial(number: u64) -> u64 {
    if number == 0 {
        1
    } else {
        number * factorial(number - 1)
    }
}
```

### Error Handling
```rust
// Use Result for fallible operations
fn read_file(path: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(path)
}

// Use Option for nullable values
fn find_user(id: u32) -> Option<User> {
    users.iter().find(|u| u.id == id).cloned()
}

// Error propagation with ?
fn process_data() -> Result<ProcessedData, Error> {
    let raw = read_file("data.txt")?;
    let parsed = parse_data(&raw)?;
    Ok(transform_data(parsed))
}

// Panic for unrecoverable errors
fn validate_input(input: &str) {
    if input.is_empty() {
        panic!("Input cannot be empty");
    }
}
```

### Testing Patterns
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_function() {
        assert_eq!(function(2), 4);
    }

    #[test]
    fn test_error_case() {
        assert!(function("invalid").is_err());
    }

    // Parameterized tests with test cases
    #[test]
    fn test_multiple_cases() {
        let test_cases = vec![
            (1, 1),
            (2, 2),
            (3, 6),
        ];
        
        for (input, expected) in test_cases {
            assert_eq!(function(input), expected);
        }
    }
}
```

### Code Structure
```rust
// File structure
//! Module documentation explaining purpose.

// Imports
use std::collections::HashMap;
use crate::other_module::function;

// Constants
const DEFAULT_TIMEOUT: u64 = 30;
static GLOBAL_VAR: &str = "global";

// Struct definitions
#[derive(Debug, Clone)]
pub struct DataProcessor {
    config: HashMap<String, String>,
}

// Implementations
impl DataProcessor {
    pub fn new(config: HashMap<String, String>) -> Self {
        Self { config }
    }
    
    pub fn process(&self, data: &[u8]) -> Result<Vec<u8>, Error> {
        // Implementation
        Ok(data.to_vec())
    }
}

// Functions
pub fn main_function() -> Result<(), Error> {
    let processor = DataProcessor::new(HashMap::new());
    processor.process(&[])?;
    Ok(())
}

// Main entry point
fn main() {
    if let Err(e) = main_function() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}
```

## Naming Conventions

- **Variables & Functions**: `snake_case` (e.g., `user_input`, `calculate_factorial`)
- **Types (Structs, Enums, Traits)**: `PascalCase` (e.g., `DataProcessor`, `UserManager`)
- **Constants**: `SCREAMING_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- **Private members**: Prefix with `_` (e.g., `_internal_helper`)
- **Modules**: `snake_case` (e.g., `flow_controls`, `variables`)

## File Organization

### Module Files
```
// 1. Module documentation (//!)
// 2. Imports
// 3. Constants and static variables
// 4. Type definitions (structs, enums, traits)
// 5. Function implementations
// 6. Module declarations (mod)
// 7. Tests (#[cfg(test)])
```

### Binary Files
```
// 1. Module documentation
// 2. Imports
// 3. Main function
// 4. Helper functions
// 5. Tests
```

## Best Practices

1. **Memory Safety**: Use Rust's ownership system properly
2. **Error Handling**: Prefer `Result` over panics for recoverable errors
3. **Testing**: Write unit tests with `#[test]` and integration tests in `tests/`
4. **Documentation**: Include doc comments for public APIs
5. **Code Quality**: Run `cargo clippy` and `cargo fmt` before commits
6. **Performance**: Use `--release` for production builds

## Configuration Files

When adding new Rust projects, include:
- `Cargo.toml` for project configuration and dependencies
- `rustfmt.toml` or `.rustfmt.toml` for custom formatting rules
- `.clippy.toml` for custom linting rules

## Common Patterns

### Iterator Usage
```rust
// Process collections efficiently
let result: Vec<i32> = numbers
    .iter()
    .filter(|&&n| n > 0)
    .map(|&n| n * 2)
    .collect();
```

### Struct Definitions
```rust
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct User {
    pub id: u32,
    pub name: String,
    email: Option<String>,
}

impl User {
    pub fn new(id: u32, name: String) -> Self {
        Self { id, name, email: None }
    }
    
    pub fn with_email(mut self, email: String) -> Self {
        self.email = Some(email);
        self
    }
}
```

### Error Types
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Parse error: {0}")]
    Parse(String),
    
    #[error("Validation failed: {field}")]
    Validation { field: String },
}
```

Remember to run quality checks before submitting changes:
```bash
cargo fmt
cargo clippy
cargo test
cargo check
```