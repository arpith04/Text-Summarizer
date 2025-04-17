import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "arpith04"
SRC_REPO = "textSummarizer"
AUTOR_EMAIL = "arpithshety5@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTOR_EMAIL,
    description="A simple text summarizer for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)