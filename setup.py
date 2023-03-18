# setup.py
from setuptools import setup, find_packages

setup(
    name="altimate_django",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["Django>=2.0", "tabulate>=0.9.0", "termcolor>=1.1.0"],
    author="Altimate Inc.",
    author_email="info@altimate.ai",
    exclude_package_data={"": ["my_tennis_club"]},
    description="A Django extension to check for various data issues",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
