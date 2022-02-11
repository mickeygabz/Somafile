
from setuptools import setup, find_packages

setup(
    name='Somafile',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='File parser into various formats',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/mickeygabz/GIT-tester',
    author='Michael M Ndirangu',
    author_email='michaelmndirangu@gmail.com'
)

