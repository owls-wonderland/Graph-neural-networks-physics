# Graph neural networks and physics


# Setting up pyenv virtual environment

## Installing pyenv

Installation is performed on a per-user basis, using the [pyenv-installer](https://github.com/pyenv/pyenv-installer):

`curl https://pyenv.run | bash`

We then need to configure our bash profile for the pyenv installation. Replace `<user>` below with your username.

```bash
echo '
export PATH="/home/<user>/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

Finally, activate the updated bash profile:

`source ~/.bashrc`

You should now be able to execute pyenv instructions:

`pyenv`

## Usage

Pyenv manages multiple environments with differing Python installations. We can see all of the Python versions available under pyenv using `pyenv pyenv install -l`.

We are now ready to create a new virtual environment. We first install the Python version of choice:

`pyenv install 3.8.2`

We can check which versions have been downloaded using `pyenv versions`.

To create a virtual environment called `toms-new-venv`, run the following:

`pyenv virtualenv 3.8.2 toms-new-venv`

Replace `toms-new-venv` with the desired environment name. We then activate the environment, in much the same way as a conda environment would be activated:

`pyenv activate toms-new-venv`

Once activated, we can check which python executable is being used by `toms-new-venv` and its version, using `which python` and `python --version`, respectively.

Installing requirements for a project is then a case of using pip, as usual:

`pip install -r requirements.txt`
