<!-- installation_and_usage.md -->

# Installation and Usage

Welcome to the installation and usage guide for the `altimate_django` library! This powerful library helps you maintain consistent data and prevent common issues in your Django projects. In this guide, we'll show you how to install the library, add it to your Django project, and run the `altimate` command to trigger the checks.

## Installation

To install `altimate_django`, simply use `pip` to install the package from PyPI:

```bash
pip install altimate_django
```

## Setup

Once you've installed the package, you need to add it to the INSTALLED_APPS section in your Django project's settings:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'altimate_django',
    # ...
]
```

### Running the Checks

To run the field checks provided by altimate_django, use Django's manage.py script and call the altimate command:

```bash
python manage.py altimate
```

This command will analyze your models' fields and report any potential issues or inconsistencies, along with actionable recommendations to improve your code quality and data consistency.

## Happy Coding!

With altimate_django installed and configured, you're ready to enhance the robustness, efficiency, and consistency of your Django applications. Enjoy building high-quality projects and be confident that your models stand the test of time!

Don't forget to check the other pages in this documentation for more information on each specific check provided by the library.
