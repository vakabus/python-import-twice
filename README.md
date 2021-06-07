# One file loaded twice

This repository demonstrates a Python module, which loads one of it source files twice and therefore contains multiple versions of the same variables.

## Running

Start with this command:

`PYTHON_PATH=. python -m test`

## Output

The output will be:
```
My name is '__main__' and I see True
My name is 'test.__main__' and I see False
My name is '__main__' and I see True
```

Expected behaviour would be:
```
My name is '__main__' and I see True
My name is '__main__' and I see False
My name is '__main__' and I see False
```