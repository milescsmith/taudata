# tau

An annotated data object format for Olink data

## Overview

tau is a Python library designed to an annotated data object format for olink data. It provides a clean, well-tested API and follows modern Python development practices.

## Features

- ✨ **Modern Python**: Built with Python 3.12+ and type hints
- 🧪 **Well Tested**: Comprehensive test suite with pytest
- 📦 **Easy Installation**: Available via pip and uv

- 🔧 **Developer Friendly**: Extensive documentation and examples
- 🚀 **Fast**: Optimized for performance
- 🛡️ **Reliable**: Robust error handling and logging

## Quick Start

### Installation

```bash
pip install tau
# or with uv
uv add tau
```

### Basic Usage



```python
from tau import main_function

# Basic usage
result = main_function()
print(result)  # "Hello from tau!"


```

## Documentation

- **[API Reference](api.md)** - Complete API documentation
- **[Examples](examples.md)** - Usage examples and tutorials
- **[Contributing](contributing.md)** - How to contribute to the project
- **[Changelog](../CHANGELOG.md)** - Version history

## Key Components

### Core Module (`tau.core`)

The core module contains the main business logic:

- `main_function()` - Primary functionality
- `calculate_statistics()` - Statistical calculations
- `validate_input()` - Input validation utilities




### Utilities (`tau.utils`)

Helper functions and utilities:

- Logging configuration
- File operations
- Environment variable handling
- Data transformation utilities



## Development

This project follows modern Python development practices:

### Tools Used

- **Package Management**: [uv](https://github.com/astral-sh/uv) for fast dependency management
- **Testing**: [pytest](https://pytest.org/) for comprehensive testing
- **Linting**: [Ruff](https://github.com/astral-sh/ruff) for fast Python linting and formatting

- **Task Automation**: [duty](https://github.com/pawamoy/duty) for development tasks
- **Documentation**: [MkDocs](https://www.mkdocs.org/) with Material theme

### Development Setup

```bash
# Clone the repository
git clone https://github.com/milescsmith/tau.git
cd tau

# Set up development environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev,docs]"

# Install pre-commit hooks
# Pre-commit not configured

# Run tests
pytest

# Run all quality checks
duty check
```

### Available Tasks

The project uses `duty` for task automation:

```bash
duty setup          # Set up development environment
duty test           # Run test suite
duty lint           # Run linting (ruff)
duty typecheck      # Run type checking
duty build          # Build package
duty docs           # Build documentation
duty publish        # Publish to PyPI
```

## Architecture

### Project Structure

```
tau/
├── src/tau/     # Source code
│   ├── __init__.py            # Package initialization
│   ├── core.py                # Core functionality
│   ├── cli.py                 # Command-line interface
│   ├── utils.py               # Utility functions
│   └── submodule/             # Optional submodules
├── tests/                     # Test suite
├── docs/                      # Documentation
├── scripts/                   # Utility scripts
└── pyproject.toml            # Project configuration
```

### Design Principles

1. **Modularity**: Clear separation of concerns
2. **Testability**: Comprehensive test coverage
3. **Documentation**: Well-documented APIs
4. **Type Safety**: Full type hint coverage
5. **Error Handling**: Robust error handling
6. **Performance**: Optimized for speed
7. **Maintainability**: Clean, readable code

## Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Support

- **Issues**: [GitHub Issues](https://github.com/milescsmith/tau/issues)
- **Discussions**: [GitHub Discussions](https://github.com/milescsmith/tau/discussions)
- **Documentation**: This documentation site
- **Email**: miles-smith@omrf.org

## License

This project is licensed under the BSD-3-Clause License. See [LICENSE.md](../LICENSE.md) for details.

## Acknowledgments

- Built with the [Python Utility Template](https://github.com/yourusername/python-utility-template)
- Powered by modern Python tooling
- Inspired by best practices from the Python community

---

*Generated with ❤️ using modern Python development practices*
