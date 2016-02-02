from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ninfo-plugin-jira',
    version=version,
    description="Jira",
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo",
        "jira",
    ],
    entry_points = {
        'ninfo.plugin': [
            'jira    =   ninfo_plugin_jira'
        ]
    }
) 
