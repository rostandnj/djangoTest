For testing this app on linux distribution (debian or ubuntu), you should follow these steps:

1) Install Python

sudo apt update

sudo apt install software-properties-common

Add the deadsnakes PPA to your system’s sources list:

sudo add-apt-repository ppa:deadsnakes/ppa

When prompted press Enter to continue:

- Press [ENTER] to continue or Ctrl-c to cancel adding it.
- Once the repository is enabled, install Python 3.9 with:

sudo apt install python3.9

- Verify that the installation was successful by typing:

python3.9 --version

2) Install Django

First you need to install PIP using this command

Download the script, from https://bootstrap.pypa.io/get-pip.py

Open a terminal/command prompt, cd to the folder containing the get-pip.py file and run:

python3.9 get-pip.py

after you can install Django from:

python3.9 -m pip install Django

3) Launch the application

in the root of the folder app you can start the app using this command:

python3.9 manage.py runserver 8000

the app will be available at this url http://127.0.0.1:8000/



