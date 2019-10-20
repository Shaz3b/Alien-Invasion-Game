#!/bin/bash -e

if [[ $(command brew -v) == "" ]]; then
  echo "Installing brew OS X."
  (/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
else
  echo "Updating brew"
  brew update
fi
  

