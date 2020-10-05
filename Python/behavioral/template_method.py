from abc import ABC, abstractmethod


class PhotoPublisher(ABC):
    """
    Abstract class
    """

    def publish_photo(self):
        """
        Template method
        """
        self.pick_photo()
        self.publish()

    def pick_photo(self):
        """
        Step with default implementation
        """
        print('Taking user to their gallery app.')

    @abstractmethod
    def publish(self):
        """
        Step that needs to be implemented in concrete classes
        """

class FacebookPublisher(PhotoPublisher):
    """
    Concrete class
    """
    def publish(self):
        print('Using Facebook API to publish the photo')


class InstagramPublisher(PhotoPublisher):
    """
    Concrete class
    """
    def publish(self):
        print('Using Instagram API to publish the photo')


class App:
    """
    Client
    """
    def publish_photo_on_facebook(self):
        FacebookPublisher().publish_photo()

    def publish_photo_on_instagram(self):
        InstagramPublisher().publish_photo()

app = App()
app.publish_photo_on_facebook()
app.publish_photo_on_instagram()
