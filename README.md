## Extension Template: Hello, Biscuit!

This template is used to initialize a new empty Biscuit extension. It includes the basic structure, tests for a simple extension that greets the user with "Hello, Biscuit!".

Check the [API reference](https://tomlin7.github.io/biscuit/api/app) for adding more functionality to your extension.

### Usage

To use this template, run the following command:

```cs
biscuit ext new <extension name>
```

### Testing

Make sure to install the extension before running the tests.

```
poetry install --with dev
```

Modify tests to reflect the changes you made to the extension. Simply run `poetry run pytest` to run the tests.

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
