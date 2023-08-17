#!/bin/bash

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git."
    exit 1
fi

# Check if any arguments are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <commit_hash_1> [<commit_hash_2> ...]"
    exit 1
fi

# Iterate through the provided commit hashes
for commit_hash in "$@"; do
    echo "Reverting commit: $commit_hash"
    git revert --no-commit $commit_hash
    
    # Check if revert was successful
    if [ $? -eq 0 ]; then
        echo "Revert successful for commit: $commit_hash"
    else
        echo "Revert failed for commit: $commit_hash"
    fi
done
