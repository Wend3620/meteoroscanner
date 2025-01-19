from setuptools import setup



setup(name = "meteoscanner",
    version = "0.1.1",
    author = "Wend3620",
    packages=['meteoscanner'],
    license_files = 'LICENSE.txt',
    license='GPLv3',
    install_requires=['metpy','cartopy', 'matplotlib', 'xarray', 'numpy', 'scipy'],
    description= "A module used for making continuous cross-section view of the atmosphere.",
    long_description= """A module used for making continuous cross-section view of the atmosphere. 
                A person working with general circulation may find this package being helpful.
                This package will also be used in other public personal projects""",
    classifiers=['License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 
                 'Intended Audience :: Science/Research'
                 ],
    long_description_content_type ='text/markdown',
    python_requires = ">=3.10")