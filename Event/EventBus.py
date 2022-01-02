class EventBus:

    subscribes = set()

    def publish_event(self, event):
        for sb in self.subscribes:
            sb.on_event(event)

    def add_subscriber(self, subscriber):
        self.subscribes.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribes.remove(subscriber)
