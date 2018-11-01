# Python playground boilerplate

This project is meant to provide the developer with a simple and easy-to-use boilerplate for exercising and experimenting with the Python language.

The developer can launch any exercise/experiment and see the output with a user-friendly CLI.

*At the beginning this project was meant to be used for the Google Developers' Machine Learning Crash Course but then I realized this could be used as a general purpose playground.*

~~# Machine Learning Crash Course~~

~~This is the playground repo for the [Google Developers'
Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)~~

## Requirements

* Python 3.7
* Pipenv

## Install dependencies

`pipenv install`

## Launch virtual environment

`pipenv shell`

## Usage

This playground makes the assumption that every exercise/experiment will be a Python function that lives inside a file whose name is in this format `module_<integer>.py`, which resides in the `exercises` folder.

The name of the function can be arbitrary.
As of today you can't pass any CLI parameter to the invoked function.

## Available commands

| Command       | Description   |
| ------------- |---------------|
| `python main.py <integer>` | list all the functions available in *module_\<integer\>* |
|`python main.py <integer> <function_name>`| invoke *function_name* from *module_\<integer\>* |

## Pylint in Visual Studio Code

In order to have Pylint working correctly in VS Code, you have
to set the path to the Python interpetrer in the `.vscode/settings.json` file.

Once you launched the virtual environment, you can retrieve the Python path
by running the command `which python` and save the output of it in the clipboard.

Then paste the content of the clipoard in the `settings.json` file,
so that your settings look like this:

```js
{
  "python.pythonPath": "<COPY CLIPBOARD CONTENT HERE>"
}
```
