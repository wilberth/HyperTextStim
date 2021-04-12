# HyperTextStim
The _HyperTextStim_ stimulus allows you to use ʜᴛᴍʟ markup in a Psychopy-like stimulus that otherwise
works much the same as the <i>TextStim</i> stimulus. _HyperTextStim_ uses pyppeteer to generate the stimulus.

## Example use
```
#!/usr/bin/env python3
from psychopy import visual
import hypertextstim

win = visual.Window([800, 600], units="pix", monitor='testMonitor')
stim = HyperTextStim(win, text="Hello <b>bold</b> world.", size=[700, 560])

while not event.getKeys():
  stim.draw()
  win.flip()
```

## Arguments
-	__text__
	_mandatory_: The html annotated text: Hello &lt;b&gt;bold&lt;/b&gt; world.</dd>

- __size__
	_optional_: Defaults to window size. Always in pixels: [800, 600]

- __backgroundColor__
	_optional_: Defaults to gray. Background color in css style: "green", "rgb(100,200,200)"

- __css__
	_optional_: Defaults to mucht the same as TextStim. suggestions (can be concatenated):
	- color: green;
	- text-align: left;
	-	text-align: justify;
	-	font-family: serif;
	-	font-size: 6mm;
