from bookshelf.models import Book
---

### 📕 `delete.md`
```markdown
# Delete Operation

```python
# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by retrieving all books
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
# (Empty queryset means the book has been deleted.)
