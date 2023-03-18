<!-- index.md -->

# Welcome to Altimate Django Library

Altimate Django is a powerful library designed to help you maintain consistent data and prevent common issues in your Django projects. By analyzing your models' fields, this library identifies potential data inconsistencies, performance issues, and other pitfalls that could negatively impact your application.

## Real-life Examples

Imagine working on a project that requires strict data validation and performance optimization. With Django Model Field Checks, you can catch issues early, improve code quality, and ensure your project maintains high standards.

### Example 1: Preventing Data Loss

Suppose you have a `UserProfile` model with a `user` field, which is a ForeignKey to the built-in `User` model. When a user is deleted, you want to avoid accidentally removing their profile data. The `ReverseCascade` check can identify this issue and recommend allowing `null` values or using a different delete rule to prevent unintended data loss:

```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Potential data loss!
```

### Example 2: Avoiding SQL Keyword Conflicts

When naming your model fields, you might unintentionally use a reserved SQL keyword, leading to unexpected behavior or SQL syntax errors. The ReservedSQLKeywords check detects fields that use reserved SQL keywords and suggests renaming them:

```python
from django.db import models

class MyModel(models.Model):
    select = models.CharField(max_length=100)  # 'select' is a reserved SQL keyword!
```

### Example 3: Ensuring Data Consistency

Numeric fields in your models should have minimum and maximum value validators to ensure data consistency and prevent out-of-range values. The MinMaxValidator check identifies fields that lack these validators and recommends adding them:

```python
from django.db import models

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)  # No MinValueValidator or MaxValueValidator!
```

Django Model Field Checks is your secret weapon for creating robust, efficient, and consistent Django applications. By catching potential issues early and providing actionable recommendations, this library empowers you to build high-quality projects that stand the test of time.

Are you ready to take your Django projects to the next level? Start using Django Model Field Checks today and unlock the full potential of your models!

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
    'altimate-django',
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
