<!-- checks/cascade_for_fk_one_to_one.md -->

# Check: Cascade for ForeignKey and OneToOneField

## Description

This check ensures that `ForeignKey` and `OneToOneField` fields are using the `CASCADE` option for the `on_delete` parameter.

## Rationale

Using `CASCADE` for the `on_delete` parameter in `ForeignKey` and `OneToOneField` fields ensures that related objects are automatically deleted when the referenced object is deleted, helping maintain database integrity. Other options, like `PROTECT`, `SET_NULL`, or `SET_DEFAULT`, may be appropriate in some cases, but using `CASCADE` is a safer default choice.

## Example

Consider the following model:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
```

The author field is a ForeignKey field, but it's not using the CASCADE option for on_delete. The check would detect this and recommend changing the on_delete option to models.CASCADE:

```python
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

However, if you have a specific reason for not using CASCADE, you should evaluate the impact on your application's data integrity and adjust the check accordingly.
