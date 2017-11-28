class StatisticsController():
    def __init__(self, book_repo, client_repo, rental_repo):
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo

    def search(self):
