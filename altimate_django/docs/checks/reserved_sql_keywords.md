<!-- checks/reserved_sql_keywords.md -->

# Check: Reserved SQL Keywords

## Description

This check identifies field names in Django models that use reserved SQL keywords. It suggests renaming the field to avoid potential issues with unexpected behavior or SQL syntax errors.

## Rationale

Using reserved SQL keywords as field names can lead to unexpected behavior or SQL syntax errors. By avoiding reserved keywords, you can prevent potential issues and maintain data consistency.

## Example

Consider the following model:

```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    select = models.CharField(max_length=100)
```

The select field is named after a reserved SQL keyword. The check would detect this and recommend renaming the field:

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
```

By renaming the field to role, you can prevent potential issues and maintain data consistency.
