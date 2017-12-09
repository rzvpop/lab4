from datetime import date, datetime, timedelta

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from repository.Repository import Repository
from validation.Validator import Validator


class ItemController():
    def __init__(self, repo):
        self._repo = repo
        self._validator = Validator()

    def getItems(self):
        return self._repo.getAll()