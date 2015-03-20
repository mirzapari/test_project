import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS = []
dependency_links = []

with open(os.path.join(os.path.dirname(__file__), 'requirements.pip')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if ("http://" in line or "https://" in line) and "#egg=" in line:
            parts = line.split("#egg=")
            REQUIREMENTS.append(parts[-1])
            dependency_links.append(line)
        elif len(line) and line[0] != "#" and line[0] != "-":
            # - covers the --extra-index-url stuff we need for local gemfury support.
            REQUIREMENTS.append(line)

setup(
    name='uber-app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    description='Awsome sauce',
    long_description="nothing to see here",
    url='https://github.com/testCompany/uber-app',
    author='testCompany',
    author_email='app@testCompany.com',
    install_requires=REQUIREMENTS,
    dependency_links=dependency_links
)
