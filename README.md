# Gnarus Warm Up

This little project looks after my workmates on the matter of warming up the alura's
env's to be deployed, instead of clicking in every little button
Now you can drink your coffee and relax a bit by the time this bot can do it for ya :)
You can also contribute to the project by reporting a problem or checking an issue.

## to run the project follow the steps bellow

By following the steps below, you'll be able to open the project on the ide of your
preference and contribute to the project if you wish for, but if you do, before you push your branch
is important to create a new .exe with your modification for the others that you use
can be beneficiaries of your improvement.
To do it the follow the step "create .exe" 

### Py lib's
Selenium

```pip install selenium```

```pip install webdriver-manager```

### Firefox

```sudo apt install firefox-geckodriver```

### tkinter

```sudo apt-get install python3-tk```

### create .exe
pyInstaller is used to create a new .exec every time we update or change something in the project,
to do so run the command below 

```pyinstaller --onefile -w main.py```

## If you just want to use the .exe file

with our .exe we will need no lib's
only the Geckodriver that's used to the selenium open and control your firefox

```sudo apt install firefox-geckodriver```

That's it, now you just need to clone the project in any local that you want and run the file WUP/dist/main.exe

![alt text](./dist/img.png)

Once everything is set up, in the running interface, you can fill in the url with the 'machine'
your email and your password, choose the environment that you are deploying, and push the START button
and wait for the bot do his thing.
