<!-- checks/excessive_blanks.md -->

# Check: Excessive Blanks

## Description

This check identifies if the `blank` attribute of fields is excessively set to `True`, which may cause issues with data consistency and validation.

## Rationale

Allowing blank values for fields that are not `ManyToManyField`, `ManyToManyRel`, or `ManyToOneRel` can lead to inconsistencies in data and validation issues. By setting `blank` to `True`, you are allowing the field to be empty in forms, which might not be suitable for all use cases.

## Example

Consider the following model:

```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    age = models.PositiveIntegerField(blank=True)
```

The username, email, and age fields have blank=True, which may lead to data inconsistency and validation issues. The check would detect this and recommend reviewing the use of blank=True in these fields:

```python
username = models.CharField(max_length=100)
email = models.EmailField()
age = models.PositiveIntegerField(null=True, blank=True)
```

In this example, we removed the blank=True attribute from the username and email fields to enforce non-empty values, while allowing the age field to be empty by setting both null=True and blank=True.

Review the use of blank=True in your model fields and determine whether it is necessary or if it should be removed.
