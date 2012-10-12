from setuptools import setup, find_packages

setup(
    name = "incuna-news",
    packages = find_packages(),
    include_package_data=True,
    version = "1.3",
    description = "Provides news.",
    author = "Incuna Ltd",
    author_email = "admin@incuna.com",
    url = "http://incuna.com/",
    install_requires = ['django-tagging>=0.3.1',]
    # download_url = "http://chardet.feedparser.org/download/python3-chardet-1.0.1.tgz",
    # long_description = """"""
)
