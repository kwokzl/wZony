import setuptools

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonWebUI",
    version="0.1.1",
    author="Zonglin Guo",
    description="Rapid HTML Construction with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kwokzl/PythonWebUI",
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)