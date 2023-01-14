# flask-server-template

Template for Flask server development.

Created using <a href = "https://www.python.org/downloads/release/python-3110/">Python v3.11</a>.

### Install Flask

`pip3 install Flask`

Read more about Flask installation <a href="https://flask.palletsprojects.com/en/2.2.x/installation/">here</a>.

<details>
  <summary>Installing virtualenv</summary>
  
  1. `cd` into the project root directory

  2. `python3 -m venv venv_name`

  The above steps create a `venv/` directory in your project where all dependencies are installed. The virtual environment needs to be activated in every terminal instance used for work in the project:

  `source venv/bin/activate`

  You should see a `(venv)` appear at the beginning of your terminal prompt indicating that you are working inside the `virtualenv`.
  
  Now when you install something like this:

  `pip install <package>`

  it will be installed to the `venv` folder and not conflict with dependencies in other projects.
</details>

<details>
  <summary>Leaving the virtual environment</summary>

  To leave the virtual environment, run:
  `deactivate`
</details>

<details>
  <summary>Run a script</summary>
  
  `python3 (script_name).py`
</details>

---

For more info about `virtualenv` and installation, see:

https://sourabhbajaj.com/mac-setup/Python/virtualenv.html


For more info about `virtualenv` installation issues, see:

https://stackoverflow.com/questions/31133050/virtualenv-command-not-found
