from setuptools import find_packages, setup

setup(
    name='lnkgui',
    packages=find_packages(include=['lnkgui']),
    version='0.1.0',
    description='Lances pygame GUI library',
    author='Yron Lance Talban',
    license='MIT'
)

# python setup.py bdist_wheel