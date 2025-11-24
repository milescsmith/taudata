# tau

An annotated data object format for Olink data

## Installation

### From PyPI (when published)

```bash
pip install tau
# or with uv
uv add tau
```

### Development Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/milescsmith/tau.git
   cd tau
   ```

2. Set up the development environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev]"
   ```
   or `uv run duty setup-dev`

3. Set up pre-commit hooks:
   ```bash
   # Pre-commit not configured
   ```


## Usage

### Python API

```python
from tau import core

# Example usage
result = core.main_function()
print(result)
```


## Development

This project uses modern Python development tools and practices:

- **Package Management**: [uv](https://github.com/astral-sh/uv) for fast dependency management
- **Testing**: [pytest](https://pytest.org/) with coverage reporting
- **Linting**: [Ruff](https://github.com/astral-sh/ruff) for fast Python linting
- **Type Checking**: [Pyright](https://github.com/microsoft/pyright) for static type analysis
- **Task Automation**: [duty](https://github.com/pawamoy/duty) for development tasks
- **Documentation**: [MkDocs](https://www.mkdocs.org/) with Material theme

### Available Tasks

Run development tasks using `duty`:

```bash
# Run tests
duty test

# Run linting and formatting
duty lint

# Build documentation
duty docs

# Build package
duty build

# Run all quality checks
duty check

# Set up development environment
duty setup
```

### Testing

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run tests in parallel
pytest -n auto
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
# Type checking not configured
```

## Project Structure

```
tau/
├── src/tau/     # Source code
├── tests/                      # Test suite
├── docs/                       # Documentation
├── scripts/                    # Utility scripts
└── pyproject.toml             # Project configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the test suite (`duty test`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Write tests for new functionality
- Follow the existing code style
- Update documentation as needed
- Ensure all tests pass before submitting PR

## License

This project is licensed under the BSD-3-Clause License - see the [LICENSE.md](LICENSE.md) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes to this project.

## Support

- **Issues**: [GitHub Issues](https://github.com/milescsmith/tau/issues)
- **Discussions**: [GitHub Discussions](https://github.com/milescsmith/tau/discussions)

---

Generated with ❤️ using the [Python Utility Template](https://github.com/rnwolf/copier-py-uv)