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
