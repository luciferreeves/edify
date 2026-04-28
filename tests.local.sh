# Clean tox environment
tox -e clean

# Sort imports
isort .

# Run Tests
tox -e check -v

# Run Docs
tox -e docs -v

# Run the tox env matching the current Python version
PY_NODOT=$(python3 -c 'import sys; print("{0.major}{0.minor}".format(sys.version_info))')
TOX_ENV="py${PY_NODOT}"

if tox --listenvs-all | grep -qE "^${TOX_ENV}$"; then
    tox -e "${TOX_ENV}" -v
else
    PY_DOTTED=$(python3 -c 'import sys; print("{0.major}.{0.minor}".format(sys.version_info))')
    echo "Python ${PY_DOTTED} (tox env ${TOX_ENV}) is not in tox envlist"
    exit 1
fi

# Run Coverage
tox -e report -v
