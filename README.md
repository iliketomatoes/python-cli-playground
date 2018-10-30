# Machine Learning Crash Course

This is the playground repo for the [Google Developers'
Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)

## Requirements

* Python 3.7
* Pipenv

## Install dependencies

`pipenv install`

## Launch virtual environment

`pipenv shell`

## Launch the app

`python main.py`

## Pylint in Visual Studio Code

In order to have Pylint working correctly in VS Code, you have
to set the path to the Python interpetrer in the `.vscode/settings.json` file.

Once you launched the virtual environment, you can retrieve the Python path
by running the command `which python` and save the output of it in the clipboard.

Then paste the content of the clipoard in the `settings.json` file,
so that your settings look like this:

```js
{
  "python.pythonPath": "< COPY CLIPBOARD CONTENT HERE >"
}
```
