## Hello Biscuit Extension Template

This template is used to initialize a new Biscuit extension. It includes the basic structure (package, tests) for a simple extension that greets the user.

Check the [API reference](https://tomlin7.github.io/biscuit/api/app) for adding more functionality to your extension.

## Getting Started

To create a new Biscuit extension using this template, you can use the [Biscuit CLI](https://pypi.org/project/biscuit-editor)(Make sure you have it installed).

```cs
biscuit ext new <extension name>
```

> [!NOTE] Make sure you have `cookiecutter` installed (`pip install cookiecutter`).

## Project Structure

Keep the structure of the project as follows to ensure compatibility with Biscuit's extension system:

```bash
your-extension/
├── src/
│   └── your_extension/
│       ├── __init__.py          # Extension entry point
│       └── extension.py         # Main extension logic
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   └── test_your_extension.py  # Test cases
├── pyproject.toml              # Project configuration
├── README.md                   # Documentation
└── .gitignore                  # Git ignore rules
```
