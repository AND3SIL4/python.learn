# Programming Languages Learning Repository

A comprehensive repository for learning programming languages through practical exercises, challenges, and real-world projects. This repository follows a structured learning path from beginner concepts to advanced implementations.

## 🎯 Learning Philosophy

This repository embraces **test-driven development (TDD)** and **project-based learning**. Each exercise includes:
- Clear problem statements
- Comprehensive test cases
- Well-documented solutions
- Progressive difficulty levels

## 📚 Repository Structure

```
languages/
├── python/                    # Python learning path
│   ├── before/               # Progressive exercises by difficulty
│   │   ├── beginner/         # Basic concepts and syntax
│   │   ├── middle/           # Intermediate topics
│   │   └── _exercices/       # Practice exercises
│   ├── challenges/           # Coding challenges with solutions
│   ├── roadmapsh/           # Roadmap.sh exercises
│   └── docs/                 # Documentation and tutorials
├── [future-languages]/       # Other languages (coming soon)
├── AGENTS.md                 # Guidelines for coding agents
└── README.md                 # This file
```

## 🐍 Python Learning Path

### Beginner Level (`python/before/beginner/`)
**Focus**: Fundamental concepts and syntax
- Variables and data types
- Basic operators
- Control flow (if/else, loops)
- Functions and scope
- Input/output operations

**Key Projects**:
- **Task Tracker** - Console-based task management system
- Basic data manipulation exercises
- Simple algorithm implementations

### Intermediate Level (`python/before/middle/`)
**Focus**: Advanced Python features
- Data structures (lists, dictionaries, sets, tuples)
- Object-oriented programming
- File handling and I/O
- Error handling and exceptions
- Decorators and generators
- Algorithm complexity analysis

**Key Topics**:
- **Data Structures** - Implementation and usage patterns
- **Algorithms** - Sorting, searching, and optimization
- **Decorators** - Function enhancement and metaprogramming
- **Exception Handling** - Robust error management

### Advanced Challenges (`python/challenges/`)
**Focus**: Problem-solving and algorithmic thinking
Each challenge follows the TDD approach:

1. **Fizz Buzz** - Classic coding interview problem
2. **Area Calculator** - Polygon area calculations
3. **String Reversal** - Manual string manipulation
4. **Binary Conversion** - Number system transformations
5. **Character Removal** - String processing
6. **Factorial Calculator** - Recursive algorithms
7. **Armstrong Numbers** - Mathematical validation
8. **Case Conversion** - String manipulation
9. **Time Parser** - Date/time processing
10. **Set Operations** - Mathematical set theory
11. **Iteration Master** - Advanced loop patterns
12. **Vector Operations** - Mathematical computations
13. **List Sorting** - Algorithm implementation

### Roadmap.sh Exercises (`python/roadmapsh/`)
**Focus**: Industry-standard exercises from roadmap.sh
- String manipulation challenges
- Data structures and algorithms
- System design fundamentals
- Best practices implementation

## 🛠️ Development Environment

### Required Tools
```bash
# Package management
brew install uv

# Code quality
pip install ruff pytest

# Virtual environment setup
uv init [project_name]
cd [project_name]
```

### Development Workflow
```bash
# 1. Create new project
uv init exercise-name
cd exercise-name

# 2. Add dependencies
uv add --dev pytest ruff

# 3. Write tests first (TDD approach)
# 4. Implement solution
# 5. Run quality checks
ruff check --fix .
ruff format .
pytest -v

# 6. Run your code
uv run python main.py
```

## 📋 Code Quality Standards

### Linting and Formatting
- **Ruff** for fast Python linting and formatting
- **Type hints** for better code documentation
- **Docstrings** for all public functions
- **PEP 8** compliance

### Testing Standards
- **Pytest** for comprehensive testing
- **Parametrized tests** for multiple scenarios
- **Exception testing** for error handling
- **Coverage reports** for quality assurance

### Code Organization
```python
# Standard file structure
"""
Module docstring explaining purpose.
"""

# Imports (standard library, third-party, local)
import os
from typing import List, Optional

# Constants
DEFAULT_VALUE = 42

# Functions
def main_function() -> None:
    """Main entry point with clear documentation."""
    pass

if __name__ == "__main__":
    main_function()
```

## 🎯 Learning Milestones

### ✅ Beginner Milestones
- [ ] Understand Python syntax and basic concepts
- [ ] Write simple functions and handle user input
- [ ] Implement basic algorithms (loops, conditionals)
- [ ] Complete the Task Tracker project

### ✅ Intermediate Milestones
- [ ] Master data structures and their applications
- [ ] Implement object-oriented programming concepts
- [ ] Handle exceptions and file operations
- [ ] Create decorators and generators
- [ ] Understand algorithm complexity

### ✅ Advanced Milestones
- [ ] Solve all 13 coding challenges
- [ ] Complete Roadmap.sh exercises
- [ ] Implement test-driven development consistently
- [ ] Write clean, maintainable, and efficient code

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd languages
   ```

2. **Set up Python environment**
   ```bash
   cd python
   uv init learning-env
   cd learning-env
   uv add --dev pytest ruff
   ```

3. **Start with beginner exercises**
   ```bash
   cd before/beginner
   # Open task-tracker.py and start learning!
   ```

4. **Follow the learning path**
   - Complete beginner exercises first
   - Progress to intermediate topics
   - Challenge yourself with coding problems
   - Implement Roadmap.sh exercises

## 📖 Additional Resources

### Documentation
- **Python Official Docs** - [python.org/docs](https://python.org/docs)
- **Roadmap.sh** - [roadmap.sh](https://roadmap.sh)
- **Test-Driven Development** - Learn TDD methodology

### Practice Platforms
- **LeetCode** - Algorithmic challenges
- **HackerRank** - Coding problems
- **Codewars** - Programming kata

### Community
- **Python Discord** - Active Python community
- **Stack Overflow** - Q&A platform
- **GitHub** - Open source contributions

## 🤝 Contributing

This is a learning repository. Contributions are welcome in the form of:
- **New exercises** - Following the established patterns
- **Improved solutions** - Better algorithms or implementations
- **Documentation** - Better explanations and guides
- **Test cases** - More comprehensive testing

## 📝 License

This repository is for educational purposes. Feel free to use, modify, and distribute the code for learning.

## 🎓 Acknowledgments

- **Roadmap.sh** for providing excellent learning paths
- **Python community** for creating amazing learning resources
- **Test-Driven Development** advocates for promoting quality code

---

**Happy Coding!** 🎉

Remember: Every expert was once a beginner. The key is consistency and practice. Start with the basics, progress gradually, and don't be afraid to make mistakes - they're part of the learning process!