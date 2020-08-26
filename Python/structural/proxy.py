class VicePresident:
    """
    proxy
    """
    def __init__(self, president):
        self.president = president

    def sign_document(self, document_topic):
        return ('VP: signing document on behalf of the president'
                if not self.is_important(document_topic)
                else self.president.sign_document(document_topic))

    def is_important(self, document_topic):
        return (True
                if document_topic in ("missile launch", "meeting with aliens")
                else False)


class President:
    """
    service
    """
    def sign_document(self, document_topic):
        return 'President: Analyzing document... Signed!'


class Meeting:
    """
    client
    """
    def __init__(self, leader):
        self.documents_topics = ['new technology', 'meeting with aliens',
                                 'subsidy']
        self.leader = leader

    def discuss_documents(self):
        for document_topic in self.documents_topics:
            print(f'debating about {document_topic}')
            response = self.leader.sign_document(document_topic)
            print(response)


# EXAMPLE USAGE
president = President()
vp = VicePresident(president)
meeting = Meeting(vp)
meeting.discuss_documents()
