from setuptools import setup

setup(name = "Scanner",
    version = "0.1.0",
    author = "Wenyuan Du",
    packages=['Scanner'],
    install_requires=['metpy','cartopy', 'matplotlib', 'xarray', 'numpy', 'scipy'])