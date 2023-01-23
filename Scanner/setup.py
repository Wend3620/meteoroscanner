from setuptools import setup

setup(name = "Scanner",
    version = "0.0.3",
    author = "Wenyuan Du",
    packages=['Scanner'],
    install_requires=['datetime','metpy','cartopy', 'matplotlib', 'xarray', 'numpy'])