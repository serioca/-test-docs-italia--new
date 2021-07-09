# test-docs-italia [![CircleCI](https://circleci.com/gh/INGV/test-docs-italia/tree/main.svg?style=svg)](https://circleci.com/gh/INGV/test-docs-italia/tree/main)

Questo e' un progetto di test per "testare":
- il template di Docs Italia come base
- un override INGV del template
- la compilazione e pubblicazione su GitHub Pages

## Debug sul proprio PC
```
$ docker run -it -v /tmp/temp_dir:/tmp/temp_dir --rm python:3.7 bash
. . .
#
# apt-get update && apt-get install -y texlive-base texlive-latex-base texlive-latex-recommended texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-formats-extra texlive-bibtex-extra texlive-humanities texlive-lang-italian texinfo texlive-science latexmk vim
. . .
#
# mkdir -p /root/project
# cd /root/project/
~/project#
~/project# git clone https://github.com/INGV/test-docs-italia.git
. . .
~/project# cd test-docs-italia
~/project/test-docs-italia# git submodule update --init --force
. . .
~/project/test-docs-italia# pip install -r requirements.txt
. . .
~/project/test-docs-italia# make html
. . .
~/project/test-docs-italia# cp -R _build/html /tmp/temp_dir/
```

## Guide
### Configurazione CircleCI + GitHub Pages
- https://circleci.com/blog/deploying-documentation-to-github-pages-with-continuous-integration/

### Sphinx:
- https://www.sphinx-doc.org/en/master/usage/configuration.html

## Sito GitHub Page
- https://ingv.github.io/test-docs-italia/
