from setuptools import setup, find_packages

setup(
    name='hours',
    version='1.1',
    packages=find_packages(),
    url='https://github.com/pclazatin/hours.git',
    description='use sqlgsheet to create and update blockytime events and post to gsheet',
    author='@pclazatin',
    long_description=open('README.md').read(),
    install_requires=open("requirements.txt", "r").read().splitlines(),
    include_package_data=True
)
