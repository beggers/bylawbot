## Install and run Ollama

### Install

```sh
brew install ollama
```

NOTE: The end of the `brew install ollama` output will tell you the correct way to run it on your computer. This is from my output which I expect to be the same for others.

### Run

To run once:

```sh
/opt/homebrew/opt/ollama/bin/ollama serve &
```

To instead start the Ollama service at boot:

```sh
brew services start ollama
```

## Python stuff

### Create and activate a virtualenv

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

To deactivate:

```sh
$ deactivate
```

### Install dependencies

```sh
pip install -r requirements.txt
```

## Do the thing

```sh
python chat.py
```
