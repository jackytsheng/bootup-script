export GIT_SSH="/usr/bin/ssh"


alias k="kubectl"

# For window 
alias sam="sam.cmd"
# Curft
alias cruft="python /c/Python39/Lib/site-packages/cruft/__main__.py"

# Can be Copy else where
# Linux command
alias ll="ls -la"
# Git Alias
alias gcb="git checkout -b"
alias gpr="git pull --rebase"
alias gcm="git checkout master"
alias gck="git checkout"
alias gc="git commit"
alias gs="git status"
alias gl="git log --oneline"

# This loads nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" 
