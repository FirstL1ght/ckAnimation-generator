import os

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    "ckAnimationGenerator", "__version__.py")

data = {}
with open(path, "r", encoding="utf-8") as f:
    exec(f.read(), data)

setuptools.setup(
    name=data["__title__"],
    version=data["__version__"],
    author=data["__author__"],
    author_email=data["__author_email__"],
    description=data["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=data["__url__"],
    packages=setuptools.find_packages(),
    install_requires=data["__install_requires__"],
    entry_points={
        "console_scripts": ["ckAnimationGenerator=ckAnimationGenerator.__main__:main"],
    },
    license=data["__license__"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
