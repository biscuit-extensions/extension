## Hello Biscuit Extension Template: {{ cookiecutter.extension_name | title }}

This template is used to initialize a new Biscuit extension. It includes the basic structure (package, tests) for a simple extension that greets the user.

Check the [API reference](https://tomlin7.github.io/biscuit/api/app) for adding more functionality to your extension.

## Extension Development

To create a new Biscuit extension, you can use the Biscuit CLI. Make sure you have the Biscuit CLI installed. If you don't have it installed, you can install it using:

```cs
biscuit ext new <extension name>
```

> [!NOTE] Make sure you have `cookiecutter` installed (`pip install cookiecutter`).

### Testing

Make sure to install the extension before running the tests.

```
poetry install --with dev
poetry run pytest
```

Modify tests to reflect the changes you made to the extension.

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
