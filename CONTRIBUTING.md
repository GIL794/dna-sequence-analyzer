# Contributing to DNA Sequence Analyzer

Thank you for your interest in contributing to DNA Sequence Analyzer! This document provides guidelines and instructions for contributing to the project.

## 🌟 Ways to Contribute

- **Report bugs** and suggest features via [GitHub Issues](https://github.com/GIL794/dna-sequence-analyzer/issues)
- **Submit pull requests** with bug fixes or new features
- **Improve documentation** by fixing typos, clarifying instructions, or adding examples
- **Share feedback** about your experience using the tool
- **Spread the word** by starring the repository and sharing with colleagues

## 🐛 Reporting Bugs

Before submitting a bug report, please:

1. **Check existing issues** to avoid duplicates
2. **Use the latest version** to ensure the bug hasn't been fixed
3. **Collect information** about your environment (OS, Python version, browser)

When submitting a bug report, include:

- **Clear title** describing the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs. actual behavior
- **Screenshots** if applicable
- **Error messages** and stack traces
- **Environment details** (Python version, OS, dependencies)

## 💡 Suggesting Features

Feature requests are welcome! Please include:

- **Use case** - Why is this feature needed?
- **Proposed solution** - How should it work?
- **Alternatives considered** - What other approaches did you think about?
- **Examples** - Provide examples from other tools if applicable

## 🔧 Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip package manager

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/dna-sequence-analyzer.git
   cd dna-sequence-analyzer
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/GIL794/dna-sequence-analyzer.git
   ```

4. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

6. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Coding Standards

### Code Style

- Follow **PEP 8** style guide
- Use **meaningful variable names** and add comments for complex logic
- Write **docstrings** for all functions and classes (Google or NumPy style)
- Add **type hints** where appropriate
- Maximum line length: 100 characters

### Running Code Formatters

```bash
# Format code with black
black src/ tests/ app.py

# Check style with flake8
flake8 src/ tests/ app.py --max-line-length=100

# Type checking with mypy
mypy src/
```

### Writing Tests

- Write tests for all new features and bug fixes
- Aim for >80% code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

```python
def test_calculate_gc_content_normal_sequence():
    """Test GC content calculation with a normal DNA sequence."""
    # Arrange
    sequence = "ATGCATGC"
    
    # Act
    result = calculate_gc_content(sequence)
    
    # Assert
    assert result == 50.0
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html --cov-report=term

# Run specific test file
pytest tests/test_sequence_analysis.py -v

# Run specific test
pytest tests/test_sequence_analysis.py::test_calculate_gc_content_normal_sequence
```

## 📤 Submitting Pull Requests

### Before Submitting

1. **Sync with upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests** and ensure they all pass:
   ```bash
   pytest tests/
   ```

3. **Check code style**:
   ```bash
   black --check src/ tests/ app.py
   flake8 src/ tests/ app.py
   ```

4. **Update documentation** if needed

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

### Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- **feat**: New feature (`feat: add motif search visualization`)
- **fix**: Bug fix (`fix: correct GC content calculation for edge cases`)
- **docs**: Documentation changes (`docs: update installation instructions`)
- **test**: Adding or updating tests (`test: add tests for ORF detection`)
- **refactor**: Code refactoring (`refactor: optimize sliding window algorithm`)
- **style**: Code style changes (`style: format code with black`)
- **chore**: Maintenance tasks (`chore: update dependencies`)

### Creating the Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create PR on GitHub**:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template

3. **PR Description should include**:
   - Summary of changes
   - Related issue numbers (e.g., "Fixes #123")
   - Testing performed
   - Screenshots (if UI changes)
   - Breaking changes (if any)

## 🔍 Code Review Process

1. **Automated checks** will run (tests, linting)
2. **Maintainers review** your code
3. **Address feedback** by pushing additional commits
4. **Approval** and merge by maintainers

### Review Timeline

- Initial response: Within 3-5 days
- Full review: Within 1-2 weeks
- Complex PRs may take longer

## 📚 Documentation Guidelines

### Code Documentation

- All public functions must have docstrings
- Include parameter types, return types, and examples
- Document any exceptions raised

```python
def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content percentage of a DNA sequence.
    
    Parameters
    ----------
    sequence : str
        DNA sequence containing A, T, G, C nucleotides.
        Case-insensitive.
    
    Returns
    -------
    float
        GC content as percentage (0-100).
    
    Raises
    ------
    ValueError
        If sequence is empty or contains invalid characters.
    
    Examples
    --------
    >>> calculate_gc_content("ATGC")
    50.0
    """
```

### User-Facing Documentation

- Keep language clear and concise
- Use examples and screenshots
- Update relevant docs when adding features
- Check for broken links

## 🏗️ Project Structure

Understanding the project structure will help you navigate the codebase:

```
dna-sequence-analyzer/
├── app.py                  # Main Streamlit application
├── src/                    # Source code modules
│   ├── sequence_analysis.py  # Core analysis functions
│   ├── sequence_io.py         # File I/O and parsing
│   ├── visualization.py       # Plotting functions
│   └── utils.py              # Helper utilities
├── tests/                  # Test suite
│   ├── test_sequence_analysis.py
│   ├── test_sequence_io.py
│   └── test_data/            # Test fixtures
├── docs/                   # Documentation
│   ├── user_guide.md
│   ├── api_documentation.md
│   ├── tutorial.md
│   └── faq.md
├── data/                   # Sample datasets
└── requirements.txt        # Python dependencies
```

## 🎯 Good First Issues

New to the project? Look for issues labeled:
- `good first issue` - Suitable for beginners
- `help wanted` - We'd appreciate community help
- `documentation` - Documentation improvements

## 🤝 Community Guidelines

- **Be respectful** and inclusive in all interactions
- **Provide constructive feedback** in code reviews
- **Help others** by answering questions in issues/discussions
- **Credit contributors** appropriately
- Follow our [Code of Conduct](CODE_OF_CONDUCT.md)

## ❓ Questions?

- Check the [FAQ](docs/faq.md)
- Search existing [issues](https://github.com/GIL794/dna-sequence-analyzer/issues)
- Start a [discussion](https://github.com/GIL794/dna-sequence-analyzer/discussions)
- Contact maintainers via support@dna-sequence-analyzer.dev

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to DNA Sequence Analyzer! Your efforts help advance bioinformatics research and education.** 🧬🔬
