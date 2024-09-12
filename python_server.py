from os import system

from SimpleWebSocketServer.SimpleExampleServer import SimpleEcho
from bokeh.io import curdoc, show, output_notebook
from bokeh.models import ColumnDataSource, Label, Button
from bokeh.plotting import figure
from bokeh.layouts import column
import random
from simple_websocket_server import WebSocketServer, WebSocket
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

# Create a plot
# Display plots in the notebook
# Create a new plot
plot = figure(title="Bokeh Text Example", x_axis_label='X', y_axis_label='Y')

source = ColumnDataSource(data=dict(x=[2], y=[2], text=["Hello, Bokeh!"]))
plot.text(x='x', y='y', text='text', source=source, text_color="blue", text_align="center", text_baseline="middle")
#button = Button(label="Clear Text")

# Define the callback function to clear the text
# def clear_text():
#     source.data = dict(x=[], y=[], text=[])
#
# # Add the callback to the button
# button.on_click(clear_text)
#
# # Layout the plot and button
# layout = column(plot, button)

# Add text to the plot
#plot.text(x=[2], y=[2], text=["Asd"], text_color="blue", text_font_size="20pt")

#label = Label(x=2, y=20, text='Sample Label')
# Show the plot
#show(plot)

# Update function
def update():
     # Open the file in read mode
    with open('str1.txt', 'r') as file:
        first_line = file.readline()
        print("now the value is"+first_line)
    source.data = dict(x=[2], y=[2], text=[first_line])
     #plot.text(x=[2], y=[2], text="   ", text_color="blue", text_font_size="20pt")
    #  str1=(int(str1)+10)
     #plot.text(x=[2], y=[2], text=[str1], text_color="blue", text_font_size="20pt")


# Add periodic callback
curdoc().add_periodic_callback(update, 1000)  # Update every second

# Add plot to document
curdoc().add_root(plot)
class SimpleEcho(WebSocket):
     str1=""
     def handleMessage(self):
         # echo message back to client
         self.sendMessage(self.data)
         str1 = self.data
         system ("echo " + str1 + ">  str1.txt")
         print(str1)

     def handleConnected(self):
         print(self.address, 'connected')

     def handleClose(self):
         print(self.address, 'closed')

server = SimpleWebSocketServer('', 5555, SimpleEcho)
server.serveforever()
