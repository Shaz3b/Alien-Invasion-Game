#!/bin/bash -e

if [[ $(command brew -v) == "" ]]; then
  echo "Installing brew on OS X."
  (/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
else
  echo "Updating brew"
  brew update
fi
  
if [[ $(command pip3 -v) == "" ]]; then
  echo "Installing pip3 on OS X."
  (python3 get-pip.py)
else
  echo "You have pip3"
fi

echo "Installing required libraries."
(pip3 install -r requirements.txt)
