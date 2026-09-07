# Dataset Quality CI/CD Demo - testing
#
This project demonstrates a CI/CD pipeline focused on validating a cleaned dataset.

Candidates:
- `release_candidate_good` -> passes all dataset quality checks
- `release_candidate_bad` -> fails because the cleaned dataset contains duplicates, missing values, and the wrong row count
- `release_candidate_fixed` -> corrected version that passes again

Dataset quality checks enforced in CI:
- approved cleaned dataset path is used
- expected row count = 5
- expected column count = 4
- no missing values
- no duplicate rows

## Recommended GitHub setup

Place this repository on GitHub with the workflow file at `.github/workflows/ci.yml`.
The matrix job runs the same CI checks against all three candidate folders.
