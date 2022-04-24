#!/bin/bash

GIT=${bamboo_capability_system_git_executable:?}
GIT_BRANCH=$($GIT rev-parse --abbrev-ref HEAD)

if ! [[ ${GIT_BRANCH} =~ ^feature/([A-Z]{2,}-[1-9][0-9]*)-.*$ ]]; then
  echo "ERROR: Unrecognised feature branch JIRA: ${GIT_BRANCH}" 1>&2
  exit 1
fi

JIRA_ID=${BASH_REMATCH[1]}

read -r SNAPSHOT_VERSION < version.txt

if ! [[ ${SNAPSHOT_VERSION} =~ ^((0|[1-9][0-9]*)(\.(0|[1-9][0-9]*)){0,2})-SNAPSHOT$ ]]; then
  echo "ERROR: Unsupported version format, expected x[.y[.z]]-SNAPSHOT, found ${SNAPSHOT_VERSION}" 1>&2
  exit 1
fi

VERSION_BASE=${BASH_REMATCH[1]}
FEATURE_VERSION=${VERSION_BASE}-${JIRA_ID}-SNAPSHOT

echo "==================================================="
echo "Feature branch: ${GIT_BRANCH}"
echo "JIRA ID: ${JIRA_ID}"
echo "Maven version: ${SNAPSHOT_VERSION}"
echo "Version base: ${VERSION_BASE}"
echo "Feature version: ${FEATURE_VERSION}"
echo "==================================================="

echo "feature.version=${FEATURE_VERSION}" > version.properties
