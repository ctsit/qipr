#!/bin/bash

export DEBIAN_FRONTEND=noninteractive
SHARED_FOLDER=/vagrant
DB_NAME=qipr
DB_USER=qipr

# import helper functions
. $SHARED_FOLDER/bootstrap_functions.sh

# Exit on first error
set -e

configure_base
install_utils
install_system_packages
install_qipr_fresh_vm
