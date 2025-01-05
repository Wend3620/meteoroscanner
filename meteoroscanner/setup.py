from setuptools import setup



setup(name = "meteoroscanner",
    version = "0.1.0",
    author = "Wend3620",
    packages=['meteoroscanner'],
    install_requires=['metpy','cartopy', 'matplotlib', 'xarray', 'numpy', 'scipy'],
    description= "A module used for making continuous cross-section view of the atmosphere.",
    classifiers=['License :: OSI Approved :: MIT License',],
    python_requires = ">=3.10")