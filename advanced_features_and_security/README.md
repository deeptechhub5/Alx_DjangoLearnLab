# Advanced Features and Security — Permissions & Groups

## Overview
This project implements Django permissions and group-based access control to manage user roles and protect resources within the application.

## Custom Permissions
In `relationship_app/models.py`, the `Book` model includes custom permissions:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

These permissions control what actions a user can perform on book entries.

## Groups and Assigned Permissions
Groups created (via Django admin):

- **Admins** → all permissions
- **Editors** → can_edit, can_create
- **Viewers** → can_view only

Each group is assigned the corresponding permissions using the Django admin panel.

## Enforcing Permissions in Views
Views are protected using:

```python
from django.contrib.auth.decorators import permission_required
