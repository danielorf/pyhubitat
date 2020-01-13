# Packaging

- Ensure the `twine` package is installed with deps: `python3 -m pip install --user --upgrade setuptools wheel twine`
- Set pypi username password env vars:
    - `export TWINE_USERNAME=XXXXXXXXXX`
    - `export TWINE_PASSWORD=XXXXXXXXXX`
- Generate dist/* files with `python setup.py sdist`
- Validate the package `twine check dist/*`
- Upload with `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`