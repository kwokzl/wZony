import setuptools

with open("./docs/PyPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wZony",
    version="0.2.0",
    author="Zonglin Guo",
    description="Quickly Build WebUI with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/kwokzl/PythonWebUI",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    project_urls={
        
        "Source": "https://github.com/kwokzl/wZony",
        "Tracker": "https://github.com/kwokzl/wZony/issues",
    },
    classifiers=[
        "LICENSE :: OSI APPROVED :: APACHE SOFTWARE LICENSE",
        "TOPIC :: INTERNET :: WWW/HTTP",
        "TOPIC :: TEXT PROCESSING :: MARKUP :: HTML",
        "PROGRAMMING LANGUAGE :: PYTHON"
    ]
)