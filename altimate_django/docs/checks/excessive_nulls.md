<!-- checks/excessive_nulls.md -->

# Check: Excessive Nulls

## Description

This check identifies non-text fields with `null=True`. Allowing null values for non-text fields can lead to inconsistent data and complicate handling of missing values. It recommends removing `null=True` for fields where null values are not expected or necessary.

## Rationale

Using `null=True` excessively for non-text fields can introduce unnecessary complexity when handling missing values. Ensuring that only fields that require null values have `null=True` can lead to cleaner data and simpler code.

## Example

Consider the following model:

```python
from django.db import models

class MyModel(models.Model):
    start_date = models.DateField(null=True)
```

The start_date field allows null values but might not need to. The check would detect this and recommend removing null=True if it's not necessary:

```python
class MyModel(models.Model):
    start_date = models.DateField()
```

By removing null=True for fields where it's not required, you can simplify handling missing values and ensure data consistency.
