# Permissions and Groups Setup in Django

## Custom Permissions
In `models.py`, we defined custom permissions on the `Article` model:
- `can_view`: Can view article list or details.
- `can_create`: Can create new articles.
- `can_edit`: Can edit existing articles.
- `can_delete`: Can delete articles.

## Groups
Configured in Django Admin:
- **Viewers**: Only have `can_view`.
- **Editors**: Have `can_view`, `can_create`, `can_edit`.
- **Admins**: Have all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Views
Permissions are enforced with the `@permission_required` decorator:
- `article_list` → requires `can_view`
- `article_create` → requires `can_create`
- `article_edit` → requires `can_edit`
- `article_delete` → requires `can_delete`

## Testing
1. Create test users.
2. Assign them to groups (Viewer, Editor, Admin).
3. Log in as each user and try accessing different views:
   - Viewer should only see list.
   - Editor should be able to view, create, and edit.
   - Admin should be able to perform all actions.
