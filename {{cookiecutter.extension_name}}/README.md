# {{ cookiecutter.extension_name | title }}

{{ cookiecutter.description }}

## 🔧 Development

### Customizing the Extension

1. **Main Extension Logic**: Edit `src/{{ cookiecutter.extension_name }}/extension.py`
2. **Entry Point**: Modify `src/{{ cookiecutter.extension_name }}/__init__.py` if needed
3. **Tests**: Update `tests/test_{{ cookiecutter.extension_name }}.py` to match your changes

### Adding New Functionality

- **`src/{{ cookiecutter.extension_name }}/extension.py`**: Contains the main `greet()` function and extension logic
- **`tests/test_{{ cookiecutter.extension_name }}.py`**: Add tests for your new functionality

## Running the Development Server

To run the development server, use the following command:

```bash
biscuit ext dev
```

This will start the server and allow you to test your extension in a local environment.

### Testing

Make sure to install `pytest` before running the tests.

```bash
biscuit ext test
```

Modify tests to reflect the changes you made to the extension.

## Publishing & Updating

To publish or update your extension, use the following commands, and follow the instructions provided by the Biscuit CLI:

```bash
biscuit ext publish
biscuit ext update
```

### Project Structure

```
{{ cookiecutter.extension_name }}/
├── src/
│   └── {{ cookiecutter.extension_name }}/
│       ├── __init__.py          # Extension entry point
│       └── extension.py         # Main extension logic
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   └── test_{{ cookiecutter.extension_name }}.py
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

---

**Author**: {{ cookiecutter.author }}  
**Version**: {{ cookiecutter.version }}
