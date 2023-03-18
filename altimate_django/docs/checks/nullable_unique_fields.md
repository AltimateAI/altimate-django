<!-- checks/nullable_unique_fields.md -->

# Nullable Unique Fields

## Description

This check identifies nullable unique fields in Django models. It suggests using a non-nullable unique field with a default value instead of allowing null values in unique fields.

## Rationale

Nullable unique fields can cause unexpected issues when multiple records have null values. Using a non-nullable unique field with a default value can help maintain data consistency and prevent potential issues.

## Example

Consider the following model:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
```

The name field is a nullable unique field. The check would detect this and recommend using a non-nullable unique field with a default value instead:

```python
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, default="")
```

By changing the name field to be non-nullable with a default value, you can prevent potential issues and maintain data consistency.
