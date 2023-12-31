import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="confspace",
    version="0.0.2",
    author="Hoonisone",
    author_email="hoonisone@gmail.com",
    description="confspace object for tuning parameter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hoonisone/confspace",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)