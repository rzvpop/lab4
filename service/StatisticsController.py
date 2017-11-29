from repository.Repository import RepositoryException


class StatisticsController():
    def __init__(self, book_repo, client_repo, rental_repo):
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo

    def search(self, repo, attr, p_str):
        '''
            Finds objects in repository by partially matching of a specified string-type attribute.
            In: repo(repository), attr(string - name o f attribute), p_str(string)
            Out: l(list of objects)
        '''

        items = repo.getAll()
        l = []

        for x in items:
            attr_value = getattr(x, attr)
            if p_str in attr_value:
                l.append(x)

        if len(l) > 0:
            return l
        raise RepositoryException("No item matches.")

    def bookSearch(self):
        pass