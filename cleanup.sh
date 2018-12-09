#!/bin/bash

branches=(measure-startup-nolayer-cold \
        measure-startup-layer-cold \
        measure-startup-nolayer-hot \
        measure-startup-layer-hot
)

for branch in "${branches[@]}"
do
  cd ${branch}
  sls remove
  cd ..
done

