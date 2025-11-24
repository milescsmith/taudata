# taudata

An annotated data object format for Olink data.

Very, *very* alpha at the moment.

## Installation

### From PyPI (when published)

```bash
pip install taudata
# or with uv
uv add taudata
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

Only one function at the moment: `read_processed_olink_parquet`

### Python API

```python
from taudata.io import read_processed_olink_parquet

# Example usage
adata = read_processed_olink_parquet(file="existing.parquet", X_col="ExtNPX", sampleid_col="sample_name",)
print(adata)
```


## Development

This project uses modern Python development tools and practices:

- **Package Management**: [uv](https://github.com/astral-sh/uv) for fast dependency management
- **Testing**: [pytest](https://pytest.org/) with coverage reporting
- **Linting**: [Ruff](https://github.com/astral-sh/ruff) for fast Python linting
- **Type Checking**: [ty](https://docs.astral.sh/ty/) for static type analysis
- **Documentation**: [MkDocs](https://www.mkdocs.org/) with Material theme
```

## Project Structure

```
tau/
├── src/taudata/   # Source code
├── tests/         # Test suite
├── docs/          # Documentation
├── scripts/       # Utility scripts
└── pyproject.toml # Project configuration
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

- **Issues**: [GitHub Issues](https://github.com/milescsmith/taudata/issues)
- **Discussions**: [GitHub Discussions](https://github.com/milescsmith/taudata/discussions)

---