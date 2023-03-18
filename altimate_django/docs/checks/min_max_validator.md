<!-- checks/min_max_validator.md -->

# Check: MinMaxValidator

## Description

This check verifies that `IntegerField` and `DecimalField` instances have both `MinValueValidator` and `MaxValueValidator` to ensure data consistency and prevent out-of-range values from being stored in the database.

## Rationale

Using `MinValueValidator` and `MaxValueValidator` for numeric fields helps maintain data integrity by enforcing minimum and maximum allowed values for the fields. This reduces the chance of storing out-of-range values and helps maintain a consistent data set.

## Example

Consider the following model:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

The price field is a DecimalField without MinValueValidator and MaxValueValidator. The check would detect this and recommend adding the validators:

```python
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
```

By using MinValueValidator and MaxValueValidator, you can ensure that the price field only accepts values within a specified range.
