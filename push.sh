#!/bin/bash

# find . -name "*.exe" | xargs rm -rf
# find . -name "*.pdb" | xargs rm -rf
git pull &&
git add . &&
git commit -m 'add' &&
git push