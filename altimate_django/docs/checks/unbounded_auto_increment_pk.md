<!-- checks/unbounded_auto_increment_pk.md -->

# Check: Unbounded Auto-Increment Primary Key

## Description

This check identifies `IntegerField` primary key fields that are auto-incrementing and do not have a maximum length set. It recommends setting a maximum value for the field to prevent potential issues with running out of primary key values.

## Rationale

Setting a maximum value for auto-incrementing primary keys helps ensure that you don't run into issues with running out of primary key values. This can prevent potential problems with data integrity and avoid unexpected behaviors in your application.

## Example

Consider the following model:

```python
from django.db import models

class MyModel(models.Model):
    id = models.IntegerField(primary_key=True)
```

The id field is an auto-incrementing primary key without a maximum length set. The check would detect this and recommend setting a maximum value:

```python
class MyModel(models.Model):
    id = models.IntegerField(primary_key=True, max_length=1000)
```

By setting a maximum value for the auto-incrementing primary key, you can prevent potential issues with running out of primary key values.
