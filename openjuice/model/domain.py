from openjuice.model.topic import Topic


class Domain:

    def __init__(self, name: str):
        self._name = name
        self._topics = []

    def add_topic(self, topic: Topic):
        self._topics.append(topic)