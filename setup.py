import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyRoboteq",
    version="0.0.9",
    author="miker2808",
    author_email="miker2808@gmail.com",
    description="Python library to ease with roboteq motor driver programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miker2808/PyRoboteq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)