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

### Testing

Make sure to install the extension before running the tests.

```
poetry install --with dev
poetry run pytest
```

Modify tests to reflect the changes you made to the extension.

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

<!--

### Publishing

To publish the extension, run the following command:

```cs
biscuit ext publish
```

### Installing

To install the extension, run the following command:

```cs
biscuit ext install <extension name>
```

-->

---

**Author**: {{ cookiecutter.author }}  
**Version**: {{ cookiecutter.version }}
