from setuptools import setup, find_packages

VERSION = '0.0.1' 
with open("README.md", "r") as fh:
    long_description = fh.read()
with open ("LICENSE", "r") as fh:
    license = fh.read()

# Setting up
setup(
        name="ft_package", 
        version=VERSION,
        author="yerkiral",
        author_email="yerkiral@student.42kocaeli.com.tr",
        description="A sample test package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license=license,
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Operating System :: Microsoft :: Windows",
        ],
)