#!/bin/bash

# SPDX-FileCopyrightText: 2022 The Calyx Institute
#
# SPDX-License-Identifier: Apache-2.0

#
# build-desc-fingerprint:
#
#   Update build.prop build description and fingerprint overrides to match stock
#
#
##############################################################################


### SET ###

# use bash strict mode
set -euo pipefail


### TRAPS ###

# trap signals for clean exit
trap 'error_m interrupted!' SIGINT

### CONSTANTS ###
readonly script_path="$(cd "$(dirname "$0")";pwd -P)"
readonly vars_path="${script_path}/../../../vendor/evolution/vars"
readonly top="${script_path}/../../.."

source "${vars_path}/pixels"

## HELP MESSAGE (USAGE INFO)
# TODO

### FUNCTIONS ###



# error message
# ARG1: error message for STDERR
# ARG2: error status
error_m() {
  echo "ERROR: ${1:-'failed.'}" 1>&2
  return "${2:-1}"
}

# print help message.
help_message() {
  echo "${help_message:-'No help available.'}"
}

main() {
  if [[ $# -ne 0 ]]; then
    local ds="${@}"
  else
    local ds="${devices[@]}"
  fi

  for d in ${ds}; do
    (
      local dv="${vars_path}/${d}"
      source "${dv}"
      local mk="$(ls ${top}/device/google/*/evolution_${d}.mk)"
      sed -i "s/${prev_build_id}/${build_id}/g" "${mk}"
      sed -i "s/${prev_build_number}/${build_number}/g" "${mk}"
    )
  done
}

### RUN PROGRAM ###

main "${@}"


##
