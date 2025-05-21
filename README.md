# Harmless Hacking
Hej! The purpose of this repo is to collect various features for changing computer settings—like desktop background, theme, or text size—through code.

In other words: how to harmlessly hack your friend's computer by sending them "test code".

P.S. The inspiration for this came from my uni friends, who used to change each other’s desktop images whenever someone left their laptop unlocked.
As an IT person, I thought—why not automate that? :)

Now I’m exploring different ways to modify system settings through code.

⚠️ Important: This is all meant in good fun. Nothing harmful. Only to be used with friends who understand the joke!


*another disclaimer - the desktop image changing code works only for Windows, as the last Ubuntu 24.04LTS closed those backdoors (but if u have older Ubu versions then everything is ok)*

---
### comming next for Linux - my ideas for later to not to forget

#### change theme
dark 
`gsettings set org.gnome.desktop.interface color-scheme prefer-dark ` 

light ` gsettings set org.gnome.desktop.interface color-scheme prefer-light.`

---
#### terminal settings 
https://askubuntu.com/questions/123268/changing-colors-for-user-host-directory-information-in-terminal-command-prompt

---
#### tutorial on bash
https://tldp.org/HOWTO/Bash-Prompt-HOWTO/

---
#### u also can use ↓ page to generate any bash u need
https://ezprompt.net/

### TO RESTORE TERMINAL CHANGES USE
`source /etc/skel/.bashrc`

---

### Other stuff just to save smwh
- show git branch in terminal `PS1='\u@\h \W$(__git_ps1 " (%s)")\$ '`
- showing weather in terminal `alias weather='curl wttr.in'`
- change the name of shortcut to another one e.g. `alias ls='sl'`
- THE BEST ONE `alias cd='echo "Access denied."'`  or `alias cd='echo "No."'` 
