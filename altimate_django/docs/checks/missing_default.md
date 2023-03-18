<!-- checks/missing_default.md -->

# Missing Default

## Description

This check identifies fields that do not have a default value and are not nullable. It recommends either providing a default value or allowing null values to prevent issues when creating new records.

## Rationale

Having a default value or allowing null values for a field can help prevent issues when creating new records. This makes it easier to handle cases where a value is not provided, ensuring that the application can continue to function smoothly.

## Example

Consider the following model:

```python
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

The bio field does not have a default value and is not nullable. The check would detect this and recommend adding a default value or allowing null values:

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', null=True)
```

By providing a default value or allowing null values for the bio field, you can prevent issues when creating new UserProfile instances without a bio value.
