# Clean tox environment
tox -e clean

# Sort imports
isort .

# Run Tests
tox -e check -v

# Run Docs
tox -e docs -v

# Get the current installed python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')

# Subset the python version to the major.minor version
PYTHON_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1,2)

if [ "$PYTHON_VERSION" = "3.7" ]; then
    # Build using python 3.7
    tox -e py37 -v
elif [ "$PYTHON_VERSION" = "3.8" ]; then
    # Build using python 3.8
    tox -e py38 -v
elif [ "$PYTHON_VERSION" = "3.9" ]; then
    # Build using python 3.9
    tox -e py39 -v
elif [ "$PYTHON_VERSION" = "3.10" ]; then
    # Build using python 3.10
    tox -e py310 -v
else
    # Show error message
    echo "Python version $PYTHON_VERSION is not supported"
fi

# Run Coverage
tox -e report -v
