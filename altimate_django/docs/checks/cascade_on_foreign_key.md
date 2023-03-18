<!-- checks/cascade_on_foreign_key.md -->

# Check: Cascade on ForeignKey

## Description

This check ensures that `ForeignKey` fields are not using the `CASCADE` option for the `on_delete` parameter and raises a warning about potential data loss.

## Rationale

Using `CASCADE` for the `on_delete` parameter in `ForeignKey` fields can lead to unexpected data loss when the referenced object is deleted. While it may be appropriate in some cases, other options like `SET_NULL` or `PROTECT` can be safer alternatives depending on the application's requirements.

## Example

Consider the following model:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

The author field is a ForeignKey field and is using the CASCADE option for on_delete. The check would detect this and recommend considering alternative options:

```python
author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
# or
author = models.ForeignKey(Author, on_delete=models.PROTECT)
```

Evaluate the impact of using CASCADE on your application's data integrity and choose the appropriate option based on your specific use case.
