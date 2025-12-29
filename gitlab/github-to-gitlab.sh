#!/bin/bash

IFS=$'\n' REPOS=($(cat repos.txt))
for REPO in "${REPOS[@]}"
do
    git clone git@github.com:"$GITHUB_ORG/$REPO".git
    cd "$REPO"

    git remote remove origin
    glab repo create "$GITLAB_ORG/$REPO"
    git remote add origin git@gitlab.com:"$GITLAB_ORG/$REPO".git
    git push -u origin master

    read -p "Delete repo? (y/N): " response
    if [[ "$response" =~ ^[Yy]$ ]]; then
      gh repo delete "$GITHUB_ORG/$REPO" --yes
    fi
done
