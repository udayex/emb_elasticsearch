#!/bin/sh

#git filter-branch --env-filter '#

#OLD_EMAIL="edward@cernera.me"
#CORRECT_NAME="udayex"
#CORRECT_EMAIL="uday@exmyb.com"

#if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
#then
#    export GIT_COMMITTER_NAME="$CORRECT_NAME"
#    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
#fi
#if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
#then
#    export GIT_AUTHOR_NAME="$CORRECT_NAME"
#    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
#fi
#' --tag-name-filter cat -- --branches --tags

git filter-branch --env-filter '
WRONG_EMAIL="edward@edward1.myfiosgateway.com"
NEW_NAME="udayex"
NEW_EMAIL="uday@exmyb.com"

if [ "$GIT_COMMITTER_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags -f
