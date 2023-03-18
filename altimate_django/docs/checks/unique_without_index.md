<!-- checks/unique_without_index.md -->

# Unique Without Index

## Description

This check identifies fields that are marked as unique (`unique=True`) but do not have a database index (`db_index=False`). It recommends adding an index to the unique field to improve query performance.

## Rationale

Adding an index to a unique field can significantly speed up lookups for unique values, making queries more efficient. This improves the overall performance of your database and can help reduce query execution time.

## Example

Consider the following model:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
```

The name field is marked as unique but does not have an index. The check would detect this and recommend adding an index:

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
```

By adding an index to the unique field, you can improve the performance of queries involving this field.
