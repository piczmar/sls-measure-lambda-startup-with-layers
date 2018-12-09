#!/bin/bash

branches=(measure-startup-nolayer-cold \
        measure-startup-layer-cold \
        measure-startup-nolayer-hot \
        measure-startup-layer-hot
)

for branch in "${branches[@]}"
do
  git clone --single-branch -b ${branch} https://github.com/piczmar/sls-aws-java-github-webhook-gitstats.git ${branch}
  cd ${branch}
  ./gradlew build
  sls deploy
  cd ..
done

