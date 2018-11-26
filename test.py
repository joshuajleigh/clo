#!/usr/bin/env python

import prompt_toolkit
import subprocess

#prompt_toolkit.shortcuts.message_dialog(
#        title="Example dialog window",
#        text="Do you want to continue?\nPress ENTER to quit.")
#
#prompt_toolkit.shortcuts.input_dialog(
#        title="Input dialog example",
#        text="Please type your name:")
#
#prompt_toolkit.shortcuts.yes_no_dialog(
#        title="Yes/No dialog example",
#        text="Do you want to confirm?")
#
#prompt_toolkit.shortcuts.button_dialog(
#        title="Button dialog example",
#        text="Do you want to confirm?",
#        buttons=[
#            ("Yes", True),
#            ("No", False),
#            ("Maybe", None)
#            ],
#        )

list_directory=subprocess.getoutput(["tree", "-L", "3", "/"])

buffer1 = prompt_toolkit.buffer.Buffer()

root_container = prompt_toolkit.layout.containers.VSplit([
    prompt_toolkit.layout.containers.Window(content=prompt_toolkit.layout.controls.BufferControl(buffer=buffer1)),
    prompt_toolkit.layout.containers.Window(width=1, char='|'),
    prompt_toolkit.layout.containers.Window(content=prompt_toolkit.layout.controls.FormattedTextControl(text=list_directory)),
])

layout = prompt_toolkit.layout.Layout(root_container)

kb = prompt_toolkit.key_binding.KeyBindings()

@kb.add('c-q')
def exit_(event):
    """
    pressing Ctrl-Q will exit the user interfact

    Setting a return value means: quit the event loop that drives the user
    interfact and return thei value from the `CommandLineInterface.run()` call.
    """
b = prompt_toolkit.key_binding.KeyBindings()

@kb.add('c-rkkkkkkkkkkkkkkkkkkkkkVyjjjjjjjjjjVpxlllllllllllllllll

app = prompt_toolkit.Application(key_bindings=kb, layout=layout, full_screen=True)
app.run()
