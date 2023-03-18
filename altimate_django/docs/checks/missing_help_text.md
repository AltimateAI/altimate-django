<!-- checks/missing_help_text.md -->

# Check: Missing Help Text

## Description

This check identifies fields that do not have `help_text` attribute set. It recommends adding `help_text` to provide a description of the field's purpose and improve user experience.

## Rationale

Help text provides additional context and guidance for users interacting with the field, such as in the Django admin interface or other forms. Adding `help_text` can improve user experience and reduce confusion.

## Example

Consider the following model:

```python
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

The bio field does not have help_text set. The check would detect this and recommend adding help_text:

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text="A brief description of the user's background.")
```

By adding help_text to the bio field, you can provide additional context and guidance for users interacting with the field.
