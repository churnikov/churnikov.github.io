import js

def ontrans(event):
    js.document.getElementById('tmp-text').innerHTML = 'Slide transition ended'

js.Reveal.on( 'slidetransitionend', ontrans)
