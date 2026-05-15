#!/bin/bash

IFS=$'\n' REPOS=($(cat repos.txt))
for REPO in "${REPOS[@]}"; do
  git clone git@gitlab.com:"$GITLAB_ORG/$REPO".git
  cd "$REPO" || exit 1

  git remote remove origin

  tea repo create --private --name "$(basename "$PWD")" --owner "$FORGEJO_ORG"
  git remote add origin "git@$FORGEJO_HOSTNAME:$FORGEJO_ORG/$REPO".git
  git push -u origin master

  curl -X 'PUT' \
    "https://${FORGEJO_HOSTNAME}/api/v1/repos/${FORGEJO_ORG}/${REPO}/topics" \
    -H "Authorization: token ${FORGEJO_TOKEN}" \
    -H 'Content-Type: application/json' \
    -d "{\"topics\": [\"${TOPIC_NAME}\"]}"
done

read -p "Delete repo? (y/N): " response
if [[ "$response" =~ ^[Yy]$ ]]; then
  for REPO in "${REPOS[@]}"; do
    glab repo delete "$GITLAB_ORG/$REPO" --yes
  done
fi
