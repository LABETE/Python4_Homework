class Publisher:
    def __init__(self):
        self.subscribers = []
        self.unsubscribers_count = 0
        self.times = 0
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        for subscriber in self.subscribers:
            times = subscriber(s)
            if times == "flag":
                self.times += 1
            if times == 3:
                self.unsubscribers_count += 1
            elif self.times == 3:
                self.unsubscribers_count += 1
                self.times = 0
        for _ in range(self.unsubscribers_count):
            self.unsubscribe(self.subscribers[0])
        self.unsubscribers_count = 0 

if __name__ == "__main__":
    def multiplier(s):
        print(2*s)
        return  "flag"
        
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.publisher = publisher
            self.name = name
            publisher.subscribe(self.process)
            self.called_times = 0
        def process(self, s):
            print(self.name, ":", s.upper())
            self.called_times += 1 
            return self.called_times
                
        def __repr__(self):
            return self.name
    
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
        