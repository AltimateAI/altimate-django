<!-- checks/large_char_field.md -->

# Large CharField

## Description

This check identifies `CharField` instances with a `max_length` value that exceeds a specified threshold (default: 255) and recommends using a `TextField` instead for storing long strings.

## Rationale

`TextField` is more efficient for storing and retrieving long text values. By using a `TextField` instead of a large `CharField`, you can improve performance and reduce the likelihood of reaching the maximum allowed length for a character field.

## Example

Consider the following model:

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
```

The content field is a CharField with a max_length of 5000, which is considered large. The check would detect this and recommend using a TextField instead:

```python
content = models.TextField()
```

By using a TextField for the content field, you can store longer text values more efficiently and avoid reaching the maximum allowed length for a character field.
