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
    #url="https://github.com/kwokzl/wZony",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    license = "Apache",
    project_urls={
        
        "Source": "https://github.com/kwokzl/wZony",
        "Tracker": "https://github.com/kwokzl/wZony/issues",
    },
    classifiers=[
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing :: Markup :: HTML",
        "Programming Language :: Python :: 3"
    ]
)