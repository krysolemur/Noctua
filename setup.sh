#!/bin/bash

# WebScope setup program 

# Installing python3 
echo -n "Installing python... "
if sudo apt install python3 > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi

# Installing pip
echo -n "Installing pip... "
if sudo apt install python3-pip > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi

# Intalling virtual enviroment
echo -n "Intalling virtual enviroment... "
if sudo apt install python3-venv > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi

# Creating virtual enviroment
echo -n "Creating virtual enviroment... "
if sudo python3 -m venv venv > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi

# Activating virtual enviroment
echo -n "Activating virtual enviroment... "
if . venv/bin/activate > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi

# Installing python packages and dependences
echo -n "Installing python packages and dependences... "
if sudo venv/bin/pip install -r requirements.txt > /dev/null 2>&1; then
    echo -e "[ \e[32mOK\e[0m ]"
else
    echo -e "[ \e[31mERROR\e[0m ]"
    exit 1;
fi
