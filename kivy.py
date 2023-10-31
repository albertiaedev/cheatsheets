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
