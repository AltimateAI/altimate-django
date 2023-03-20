<!-- index.md -->

# Welcome to Altimate Django Library

Altimate Django is a powerful library designed to help you maintain consistent data and prevent common issues in your Django projects. By analyzing your models' fields, this library identifies potential data inconsistencies, performance issues, and other pitfalls that could negatively impact your application. The tool is designed to help developers identify and prevent potential issues in their Django models. We have classified the checks implemented in the tool according to the types of issues they can catch: data loss, data corruption, data inconsistency, and other. Understanding these categories will help developers better address the issues detected by the tool and improve the overall quality and integrity of their Django applications.

## Data Loss

- **ReverseCascade**: Ensures that a ForeignKey or OneToOneField is not set to CASCADE delete and allows null values, preventing unintended data loss when related records are deleted.
- **CascadeForFKOneToOne**: Checks if a ForeignKey or OneToOneField uses CASCADE delete and does not allow null values, preventing unintended data loss when related records are deleted.
- **InappropriateCascade**: Verifies that CASCADE is not being used inappropriately on ForeignKey fields, preventing unintended data loss when related records are deleted.

## Data Corruption

- **MissingDefault**: Ensures that fields with null=False have a default value specified to avoid potential data corruption.
- **UniqueWithoutIndex**: Verifies that unique constraints are created with indexes to prevent data corruption due to slow queries.

## Data Inconsistency

- **MinMaxValidator**: Checks if MinValueValidator and MaxValueValidator are applied to numeric fields, ensuring data consistency and preventing out-of-range values.
- **ExcessiveNulls**: Ensures that fields are not unnecessarily set to allow null values, preventing data inconsistency.
- **NullableUniqueFields**: Checks if unique fields are set to allow null values, preventing data inconsistency.
- **UnboundedAutoIncrementPK**: Verifies that models with auto-incrementing primary keys have a maximum value set, preventing data inconsistency due to running out of primary key values.
- **CascadeOnForeignKey**: Ensures that ForeignKey fields have appropriate on_delete behavior to maintain data consistency.
- **LargeCharField**: Verifies that CharField maximum lengths are set to reasonable values to maintain data consistency.
- **ExcessiveBlanks**: Ensures that fields are not unnecessarily set to allow blank values, preventing data inconsistency.

## Other

- **ReservedSQLKeywords**: Verifies that model and field names do not use reserved SQL keywords, preventing potential naming conflicts and issues.
- **ForeignKeyNaming**: Ensures that the naming convention for ForeignKey fields follows the format: "{related_model_name.lower()}\_id".
- **MissingHelpText**: Checks if fields have help_text specified, improving user experience and reducing confusion.

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

## Sample Output

![img] (./imgs/output.png "Sample Output")
