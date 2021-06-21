# coding: utf-8

"""
    SerpsBot

    Our APIs allow data miners to harvest huge volumes of data from Google and other search engines.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "serpsbot-api"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SerpsBot",
    author_email="",
    url="https://github.com/serpsbotapi/serpsbot-python",
    keywords=["Swagger", "SerpsBot"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Our APIs allow data miners to harvest huge volumes of data from Google and other search engines.  # noqa: E501
    """
)
