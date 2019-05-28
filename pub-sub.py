import gtk
import logging

subscriptions = {}

def subscribe(message, subscriber):
    
    if not message in subscriptions:
        subscriptions[message] = [subscriber]
    else:
        subscriptions[message].append(subscriber)
        
def publish(message, *args, **kwargs):
    if not message in subscriptions:
        logging.info("Message not found")
        return
    for subscriber in subscriptions[message]:
        try:
            subscriber(*args, **kwargs)
        except Exception, e:
            logging.error("There is some error ")
            
def unsubscribe(message, subscriber):
    if not message in subscriptions:
        logging.info("Message not found")
    else:
        subscriptions[message].remove(subscriber)
        
