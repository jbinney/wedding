# Joe and Bistra's Wedding Site

This is a simple Django app for our wedding site, which includes an RSVP system and some basic informational pages. This site uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to manage Python dependencies, [Bootstrap](http://getbootstrap.com/) for simple UI components and styling, and [jQuery](https://jquery.com/) mostly just because it's a Bootstrap dependency ;)

Please feel free to fork this project for your own wedding site!

## Setup

1. Install pip [(instructions here)](http://python-packaging-user-guide.readthedocs.org/en/latest/installing/).

1. Install virtualenvwrapper:

  ```bash
  $ sudo pip install virtualenvwrapper
  ```
  
  *Note: You might need [this workaround](http://stackoverflow.com/a/33425578) for OS X 10.11.*
  
1. Set up virtualenvwrapper:
  1. Add the following lines to your shell startup file:

    ```bash
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/projects # This should be where your cloned repos live
    source /usr/local/bin/virtualenvwrapper.sh
    ```
    
  1. Reload the startup file (e.g., run `source ~/.bashrc`).

1. Set up a virtualenv for this project:

  ```bash
  $ mkvirtualenv wedding
  ```
  
1. Install python dependencies into the virtualenv:

  ```bash
  $ pip install -r requirements.txt
  ```
  
1. Initialize the database:

  ```bash
  $ ./manage.py migrate
  ```
  
1. Run the web server:

  ```bash
  $ ./manage.py runserver
  ```
  
  You can now view the site at http://127.0.0.1:8000/.
