from abc import ABC, abstractmethod


class Subscriber(ABC):
    """
    Subscriber interface
    """

    @abstractmethod
    def update(self):
        pass


class EmailSubscriber(Subscriber):
    """
    Concrete subscriber
    """
    def __init__(self, email_direction: str):
        self.email_direction = email_direction
    
    def update(self):
        self.send_email()

    def send_email(self):
        print(f"Sending email to {self.email_direction}")


class TwitterSubscriber(Subscriber):
    """
    Another concrete subscriber
    """
    def __init__(self, username: str):
        self.username = username
    
    def update(self):
        self.run_bot()

    def run_bot(self):
        print(f"Twitter bot is twitting {self.username}")


class Article:
    """
    Articles to be published in a blog
    """
    def publish(self):
        print(f'The article has been published')


class Blog:
    """
    Publisher class.
    """
    def __init__(self):
        self.subscribers = list()

    def publish_new_article(self, article: Article):
        article.publish()
        self.notify_subscribers()

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)


# USAGE
cool_blog = Blog()
cool_blog.subscribe(EmailSubscriber('bob@example.com'))
cool_blog.subscribe(TwitterSubscriber('@revliscano'))

new_article = Article()
cool_blog.publish_new_article(new_article)
