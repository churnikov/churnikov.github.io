# PyScript

Python in the browser

----

[pyscript.net](https://pyscript.net/)

<iframe src="https://pyscript.net/" width="100%" height="600"></iframe>

----

- Something **standard** could be done via **PyScript**
- Something **custom** could be done via **Pyodide**

----
Let's see it in action
```html[2-3|6-10]
<head>
    <link rel="stylesheet" type="text/css" href="https://pyscript.net/releases/2023.11.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2023.11.1/core.js"></script>
</head>
<body>
    <div id="output-demo-1"></div>
    <script type="py" target="output-demo-1">
        from pyscript import display
        display("Hello world!")
    </script>
</body>
```
Open [demo-1.html](assets/demos/demo-1.html)

----

But micropython is even faster to load

```html[|3]
<body>
    <div id="output-demo-1"></div>
    <script type="mpy" target="output-demo-1">
        from pyscript import display
        display("Hello world!")
    </script>
</body>
```
Open [demo-2-micropython.html](assets/demos/demo-2-micropython.html)

----
We can also make PyScript interact with the presentation!
<div>
    <button py-click="say_hi">Click Me!</button>
    <div class="info-icon">
        ℹ️
        <div style="width: 600px" class="tooltip">
            <div class="code-snippet">
                <pre style="all: initial; font-size: 20px">
                <code>
<div id="output-demo-1"></div>
<script type="py">
    from pyscript import display
    def say_hi(event):
        display(f"Hi from pyscript!", target="output-demo-1")
        display(f"Triggered by {event}", target="output-demo-1")
</script>
                </code>
            </div>
        </div>
    </div>
</p>

<div id="output-demo-1"></div>

<script type="py">
    from pyscript import display
    def say_hi(event):
        display(f"Hi from pyscript!", target="output-demo-1")
        display(f"Triggered by {event}", target="output-demo-1")
</script>

---

# Importing stuff from stdlib

----

[stdlib-demo](http://localhost:2500/assets/demos/stdlib_demo.html)

----

```py[|1]
		<button py-click="get_random_number">Get random number</button>
		<div id="output"></div>
		<script type="py" target="output">
from pyscript import display
from random import randint
def get_random_number(event):
		display(str(randint(0, 100)))
		</script>

```

<p class="fragment">
    We can handle events like following this template: py-[event]
</p>


<a href="https://jeff.glass/post/whats-new-pyscript-2023-11-1/#events">About events handlers</a>

---

# Importing stuff from PyPI

----

### 1. Python packages are added via config

```html[4-5|7-9]
<head>
...
<!-- "Installation" of PyScript -->
<link rel="stylesheet" href="https://pyscript.net/releases/2023.11.1/core.css" />
<script type="module" src="https://pyscript.net/releases/2023.11.1/core.js"></script>
<!-- Configuration of PyScript -->
<py-config type="toml">
    packages = ["numpy", "matplotlib"]
</py-config>
```

[https://docs.pyscript.net/latest/reference/elements/py-config.html](https://docs.pyscript.net/latest/reference/elements/py-config.html)

[https://pyodide.org/en/stable/usage/packages-in-pyodide.html](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)


----

> Actually, for this example, I'm using PyScript 2023.05.1

<iframe src="assets/demos/numpy_plot_demo.html" width="70%" height="600"></iframe>

[https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py](https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py)

---

# Web workers

[Docs](https://docs.pyscript.net/2023.11.1/user-guide/workers/)

----

<!-- <div id="output-worker"></div> -->

<!-- <script type="mpy" target="output-worker"> -->
<!--     from pyscript import display -->
<!--     display(f"hello, world! {1+2=}") -->
<!-- </script> -->

<!-- <script type="py" target="output-worker" worker> -->
<!--     from pyscript import display -->
<!--     display("first worker") -->
<!--     x = 1 -->
<!--     display(f"{x=}") -->
<!-- </script> -->

<!-- <script type="py" target="output-worker" worker> -->
<!--     from pyscript import display -->
<!--     display("second worker") -->
<!--     display(f"{x=}") # Error - each 'worker' tag is a separate worker -->
<!-- </script> -->


<!-- ---- -->

<!-- <button py-click="start_worker">Start worker</button> -->
<!-- <div id="output-worker-1"></div> -->
<!-- <script type="py" target="output-worker-1" worker> -->
<!--     from pyscript import display -->
<!--     from functools import count -->
<!--     def start_worker(event): -->
<!--         counter = count() -->
<!--         while True: -->
<!--             display(f"worker: {next(counter)}") -->
<!-- </script> -->

---

# Projects built on Pyodide

- [Jupyter lite](https://jupyter.org/try-jupyter/lab/)
- [Gradio lite](https://www.gradio.app/guides/gradio-lite)
- [Stlite](https://github.com/whitphx/stlite)

[Source Pyodide>Related Projects](https://pyodide.org/en/stable/project/related-projects.html)

---

# Downsides of PyScript

1. Heavily depends on the internet _so_ Might be slow to load
2. Still in development _so_ bugs, rapid api changes
3. Early adoption _so_ Is not friends yet with some tools established (i.e. VUE)

---

# Resources

- **Docs**
- [PyScript](https://pyscript.net/)
- [This blog from Jeff Glass is sometimes better then the official docs](https://jeff.glass/)
- **Talks/Blogs**
- [PyCon US 2023 PyScript slides](https://jeff.glass/post/pycon23-slides/)
- [How to interact with a backend with PyScript](https://docs.pyscript.net/latest/tutorials/requests.html)
- [PyScript - what you need to know by Nicholas H. Tollervey](https://www.youtube.com/watch?v=ocpVSExSDvw&t=3s&pp=ygUVTmljaG9sYXMgSC4gVG9sbGVydmV5)
- [Build a webapp with Flask and PyScript](https://www.youtube.com/watch?v=WZRNbspsjFM)
- [Build a webapp with Django and PyScript](https://www.youtube.com/watch?v=zw4V48Al8LU)
- [How to secure your api](https://medium.com/swlh/3-ways-to-secure-your-web-api-for-different-situations-8d5cd4762ab3)
- [PyScript: A Useful Abomination?](https://medium.com/analytics-vidhya/pyscript-a-useful-abomination-adc1f550c4be)


