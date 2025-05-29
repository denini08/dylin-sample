#!/bin/bash

set -ex

# set the working directory and package details
WORK_DIR="/app/mypackage"
PACKAGE_NAME="mypackage"
TEST_MODULE="mypackage.tests.test_inconsistent_preprocessing"
OUTPUT_DIR="/tmp/dynapyt_output"

# generate a unique session ID for the DynaPyt run
export DYNAPYT_SESSION_ID=$(uuidgen)
echo "DynaPyt Session ID: $DYNAPYT_SESSION_ID"

# create output directory
mkdir -p "$OUTPUT_DIR-$DYNAPYT_SESSION_ID"

# navigate to the working directory
cd "$WORK_DIR"

# select analyses
python3 -m dylin.select_checkers \
    --include="All" \
    --exclude="None" \
    --output_dir="${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}" > analyses.txt

mv /app/mypackage/analyses.txt "${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}/analyses.txt"

# instrument the code
python3 -m dynapyt.run_instrumentation \
    --directory="/app" \
    --analysisFile="${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}/analyses.txt"

# pwd
mv "${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}/analyses.txt" "/tmp/dynapyt_analyses-${DYNAPYT_SESSION_ID}.txt"

pytest | tee "${TEST_MODULE##*.}_Output.txt" 2>&1

# generate findings report
python3 -m dynapyt.post_run \
    --coverage_dir="" \
    --output_dir="${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}"

python3 -m dylin.format_output \
    --findings_path="${OUTPUT_DIR}-${DYNAPYT_SESSION_ID}/output.json" > "${TEST_MODULE##*.}_findings.txt"

cat "${TEST_MODULE##*.}_findings.txt"


echo "[INFO] Done."