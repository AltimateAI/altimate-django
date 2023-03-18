<!-- checks/reverse_cascade.md -->

# Reverse Cascade

## Description

This check identifies `ForeignKey` or `OneToOneField` instances with the `CASCADE` delete rule that do not allow null values. It recommends allowing null values or using a different delete rule to prevent unintended data loss when related records are deleted.

## Rationale

Allowing null values in a `ForeignKey` or `OneToOneField` with the `CASCADE` delete rule helps prevent unintended data loss when related records are deleted. It ensures that when a related object is deleted, the field in the current object is set to `NULL` instead of causing the current object to be deleted as well.

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

The author field is a ForeignKey with the CASCADE delete rule and does not allow null values. The check would detect this and recommend allowing null values or using a different delete rule:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
```

By allowing null values for the author field or changing the delete rule, you can prevent unintended data loss when related records are deleted.
