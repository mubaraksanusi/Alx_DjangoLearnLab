# LibraryProject

This is the **LibraryProject** for the ALX Django learning tasks.  
It demonstrates:

1. **Custom User Model** with:
   - `date_of_birth` (DateField)
   - `profile_photo` (ImageField)

2. **Bookshelf App** with:
   - `Book` model including `can_create` and `can_delete` permissions
   - Full CRUD views for books (`add`, `edit`, `delete`)
   - `book_list` view protected with `@permission_required(..., raise_exception=True)`

3. **Relationship App** (for advanced model relationships):
   - `Author` → `Book` (ForeignKey)
   - `Library` → `Book` (ManyToMany)
   - `Librarian` → `Library` (OneToOne)

## Project Structure

