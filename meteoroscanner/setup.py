from setuptools import setup



setup(name = "meteoroscanner",
    version = "0.1.0",
    author = "Wend3620",
    packages=['meteoroscanner'],
    license_files = 'LICENSE.txt',
    license='GPLv3',
    install_requires=['metpy','cartopy', 'matplotlib', 'xarray', 'numpy', 'scipy'],
    description= "A module used for making continuous cross-section view of the atmosphere.",
    long_description= """A module used for making continuous cross-section view of the atmosphere. 
                A person working with general circulation may find this package being helpful.
                This package will also be used in other public personal projects""",
    classifiers=['License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 
                 'Topic :: General Circulation',
                 'Topic :: Meteorology',
                 'Intended Audience :: Science/Research'
                 ],
    python_requires = ">=3.10")