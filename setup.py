import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlake",
    version="0.0.3",
    author="Abhishek Upperwal",
    author_email="mesh@soket.in",
    description="Dynamic timer to learn the update frequency of a resource on the web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/upperwal",
    packages=setuptools.find_packages(),
    package_dir={'':'src'},
    py_modules=['dlake'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pymongo'
    ]
)