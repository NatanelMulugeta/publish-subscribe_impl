import pygtk
pygtk.require('2.0')
import gtk
   
MESSAGE = "This is the message"

def subscriberArg(some, data):
    print("Received: ", some, data)

class Message:
    def callback(self, widget, data=None):
        publish(MESSAGE, "an", " invitation")

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("This is the window title")
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())
        self.window.set_border_width(10)

        
def main():
    # subscribing
    subscribe(MESSAGE, subscriberArg)
    gtk.main()
    return 0     

if __name__ == "__main__":
    Message()
    main()
