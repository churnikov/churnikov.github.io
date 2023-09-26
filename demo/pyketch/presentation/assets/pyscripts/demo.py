import js
from pyscript import when

@when("click", selector="#say-hi-button")
def say_hi(event):
    display(f"Hi from pyscript!", target="say-hi-log")
    display(f"Triggered by {event}", target="say-hi-log")

