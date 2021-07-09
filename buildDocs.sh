#!/bin/bash
set -x
################################################################################
# File:    buildDocs.sh
# Purpose: Script that builds our documentation using sphinx and updates GitHub
#          Pages. This script is executed by:
#            .github/workflows/docs_pages_workflow.yml
#
# Authors:
# Created: 2021-07-09
# Updated:
# Version: 0.1
################################################################################

# make a new temp dir which will be our GitHub Pages docroot
docroot='_build'

mkdir -p "${docroot}"/it
mkdir -p "${docroot}"/en

sphinx-build -b html it "${docroot}"/it -D language=it
sphinx-build -b html en "${docroot}"/en -D language=en

# add redirect from the docroot to our default docs language/version
cat > "${docroot}"/index.html <<EOF
<!DOCTYPE html>
<html>
   <head>
      <title>helloWorld Docs</title>
      <meta http-equiv = "refresh" content="0; url='it/'" />
   </head>
   <body>
      <p>Please wait while you're redirected to our <a href="/it/">documentation</a>.</p>
   </body>
</html>
EOF

# exit cleanly
exit 0