<!-- checks/foreign_key_naming.md -->

# ForeignKey Naming

## Description

This check ensures that the naming convention for `ForeignKey` fields in a Django model follows the format: `{related_model_name.lower()}_id`.

## Rationale

Following a consistent naming convention for `ForeignKey` fields improves code readability and maintainability. It makes it easier for developers to understand the relationships between models and work with the codebase.

## Example

Consider the following model:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
```

The writer field is a ForeignKey field, but its name does not follow the naming convention. The check would detect this and recommend changing the field name to author_id:

```python
author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
```

By following the naming convention, developers working with the code can easily understand the relationship between Book and Author models.
