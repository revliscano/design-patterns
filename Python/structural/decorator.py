from abc import ABC, abstractmethod


class Article:
    """
    component
    """
    def publish(self):
        print('-article has been published-')


class BaseDecorator:
    """
    Base decorator
    """
    def __init__(self, article):
        self.article = article

    def publish(self):
        self.article.publish()

    
class TranslationDecorator(BaseDecorator):
    """
    Concrete decorator
    """
    def publish(self):
        self.translate()
        super().publish()

    def translate(self):
        print('translating article...')


class Blog:
    """
    client
    """
    def __init__(self):
        self.newest_article = None

    def create_new_article(self, language):
        print('creating a new article...')
        self.newest_article = (Article() if language == 'en'
                               else TranslationDecorator(Article()))

    def publish_article(self):
        if self.newest_article:
            self.newest_article.publish()    


# EXAMPLE USAGE
blog = Blog()
blog.create_new_article('it')
blog.publish_article()
blog.create_new_article('en')
blog.publish_article()
blog.create_new_article('fr')
blog.publish_article()
