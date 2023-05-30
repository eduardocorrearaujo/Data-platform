from typing import List, Optional
from ninja import Router
from django.shortcuts import get_object_or_404

from .models import Author
from .schema import Schema, AuthorSchema, NotFoundSchema


router = Router()

# -- Author Model --
class AuthorSchemaIn(Schema):
    """ Input for the request's body """
    name: str


@router.get('/authors/', response=List[AuthorSchema])
def list_authors(request, name: Optional[str] = None):
    """ Lists all authors, can be filtered by name """
    if name:
        return Author.objects.filter(name__icontains=name)
    return Author.objects.all()

@router.get('/authors/{author_id}', response={200: AuthorSchema, 404: NotFoundSchema})
def get_author(request, author_id: int):
    """ Gets author by id """
    try:
        author = Author.objects.get(pk=author_id)
        return (200, author)
    except Author.DoesNotExist as e:
        return (404, {"message": "Author not found"})

@router.post('/authors/', response={201: AuthorSchema})
def create_author(request, payload: AuthorSchemaIn):
    """ Posts author to database """
    author = Author.objects.create(**payload.dict())
    return (201, author)

@router.put('/authors/{id}', response=AuthorSchema)
def update_author(request, id: int, payload: AuthorSchemaIn):
    """ Updates author """
    author = get_object_or_404(Author, id=id)

    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    
    author.save()
    return author

@router.delete('/authors/{id}', response={204: None})
def delete_author(request, id: int):
    """ Deletes author """
    author = get_object_or_404(Author, id=id)
    author.delete()
    return (204, None)
