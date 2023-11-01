#KIVY CHEATSHEET

# Imports
from kivy.app import App
from kivy.uix.label import Label

# Create a label widget
label = Label(text='Hello, Kivy!')

# Add the label widget to the root widget
root.add_widget(label)

# Create a box layout
box_layout = BoxLayout(orientation='vertical')

# Add the label widget to the box layout
box_layout.add_widget(label)

# Add the box layout to the root widget
root.add_widget(box_layout)

# Define an event handler
def on_button_press(button):
    print('Button pressed!')

# Create a button widget
button = Button(text='Press Me!')

# Bind the button press event to the event handler
button.bind(on_press=on_button_press)

# Add the button widget to the root widget
root.add_widget(button)

# KV file
[Screen]
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Hello, Kivy!'
    Button:
        text: 'Press Me!'
        on_press: app.on_button_press()

# Python code
class MyApp(App):
    def build(self):
        return Builder.load_file('my_kv_file.kv')

    def on_button_press(self):
        print('Button pressed!')

if __name__ == '__main__':
    MyApp().run()

# Build the app for Android
buildozer android debug

# Build the app for iOS
buildozer ios debug

# Build the app for Windows
buildozer win64 debug


'''
This is an example of how to build a Kivy app
'''

# Import the necessary modules
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

# Create a label widget
label = Label(text='Hello, Kivy!')

# Create a button widget
button = Button(text='Click Me!')
