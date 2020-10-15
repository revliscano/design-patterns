from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, name):
        self.name = name
        self.path = ''

    @abstractmethod
    def delete(self):
        pass


class File(Element):        
    def delete(self):
        print(f'{self.path}{self.name} has been deleted')


class Folder(Element):
    def __init__(self, name):
        super().__init__(name)
        self.elements = []

    def add(self, element):
        element.path = f'{self.path}{self.name}/'
        self.elements.append(element)

    def delete(self):
        for element in self.elements:
            element.delete()


class App:
    def delete_descendants(self, folder):
        folder.delete()


root = Folder('C:')
users = Folder('Users')
rafael = Folder('Rafael')
text_file = File('file_1.txt')
music_file = File('file_2.mp3')
video_file = File('file_3.mp4')
work = Folder('Work')
readme = File('README.md')
python_folder = Folder('Python')
python_file = File('file_4.py')
js_folder = Folder('JS')
js_file = File('file_5.js')

root.add(users)
users.add(rafael)
rafael.add(text_file)
rafael.add(music_file)
rafael.add(video_file)
rafael.add(work)
work.add(readme)
work.add(python_folder)
work.add(js_folder)
python_folder.add(python_file)
js_folder.add(js_file)

app = App().delete_descendants(root)
