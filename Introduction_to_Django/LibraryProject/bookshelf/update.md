# Update Book Title

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
```
# Expected Output:
# 'Nineteen Eighty-Four'
