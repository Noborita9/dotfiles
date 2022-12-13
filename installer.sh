#!/bin/bash


mkdir ~/.config/picom ~/.config/alacritty

sudo ln ./alacritty/alacritty.yml ~/.config/alacritty
sudo ln ./tmux/.tmux.conf ~/.tmux.conf
sudo ln ./picom/picom.conf ~/.config/picom/picom.conf
sudo ln ./shell/.zshrc ~/.zshrc
