from setuptools import setup, find_packages

setup(
    name="ACIT4420_File_Organizer",  # The package name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="A tool for sorting files into folders mathing their file extension",
    author="Martin Solevåg Glærum",
    author_email="magla7524@oslomet.no",
    entry_points={
        'console_scripts': [
            'file_organizer=file_organizer.main:main',  # Points directly to the main function in main.py
        ],
    },
)
