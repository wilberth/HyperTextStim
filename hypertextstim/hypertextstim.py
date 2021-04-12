#!/usr/bin/env python3
import tempfile
import asyncio
import pyppeteer
from psychopy import core, visual, event, clock

text = """
<h1>HyperTextStim</h1>
<p>The <i>HyperTextStim</i> stimulus allows you to use ʜᴛᴍʟ markup in a Psychopy-like stimulus that otherwise
works much the same as the <i>TextStim</i> stimulus. <i>HyperTextStim</i> uses pyppeteer to generate the stimulus.

<h2>Example use</h2>
<pre>
from psychopy import visual
import hypertextstim

win = visual.Window([800, 600], units="pix", monitor='testMonitor')
stim = HyperTextStim(win, text="Hello &lt;b&gt;bold&lt;/b&gt; world.", size=[700, 560])

while not event.getKeys():
  stim.draw()
  win.flip()
</pre>

<h2>Arguments</h2>
<dl>
	<dt>text</dt>
	<dd>The html annotated text: Hello &lt;b&gt;bold&lt;/b&gt; world.</dd>

	<dt>size</dt>
	<dd>Default to window size. Always in pixels: [800, 600]</dd>

	<dt>backgroundColor</dt>
	<dd>Background color in css style: "green", rgb(100,200,200)</dd>

	<dt>css</dt>
	<dd>suggestions:
		<ul> 
			<li>color: green;</li>
			<li>text-align: left;</li> 
			<li>text-align: justify; </li>
			<li>font-family: serif;</li> 
			<li>font-size: 6mm;</li>
		</ul>
	</dd>
</dl>

<p>
"""

template = """
<html>
<head>
<style>
body{
  display: flex;
	font-family: sans-serif;
	font-size: 20px;
	background-color: %s;
}
.element{
	align-self: center;
	margin: 0 auto;
	color: white;
	text-align: center;
	%s
}
</style>
</head>
<body>
<div class=element>
%s
</div>
</body>
</html>
"""

class HyperTextStim(visual.ImageStim):
	"""
	turn HTML into image and show as ImageStim, default size is the window size
	keyword arguments:
		- size, always in pixels
		- text, html formatted text
		- css, stylesheet which is appended to the default style sheet which mimics the TextStim look
			suggestions (just concatenate them): 
				- text-align: left; 
				- text-align: justify; 
				- font-family: serif; 
				- font-size: 6mm;
				- color: green;
		- backgroundColor, in css style: "green", rgb(100,200,200)
		- pos
	- todo: size in other units than pix
	"""
	def __init__(self, *args, **kwargs):
		# size for pyppeteer
		try:
			self.isize = kwargs["size"] # stimulus size
		except:
			self.isize = [args[0].clientSize[0].item(), args[0].clientSize[1].item()] # window size
		# position for imagestim, todo: psychopy units
		try:
			pos = kwargs["pos"] # stimulus size
		except:
			pos = [0,0]
		# optional style 
		try:
			self.css = kwargs["css"] # stimulus size
		except:
			self.css = ""
		try:
			self.backgroundColor = kwargs["backgroundColor"] # stimulus size
		except:
			self.backgroundColor = "gray"
		self.args = args
		self.kwargs = kwargs
		self.tempFile = tempfile.mkdtemp(prefix='hypertextstim_') + ".png"
		asyncio.get_event_loop().run_until_complete(self.render())
		super().__init__(args[0], image=self.tempFile, pos=pos)
		
	async def render(self):
		browser = await pyppeteer.launch()
		page = await browser.newPage()
		await page.setViewport({"width": self.isize[0], "height": self.isize[1]})
		await page.goto("data:text/html;charset=utf-8," + template % (self.backgroundColor, self.css, self.kwargs["text"]))
		await page.screenshot({"path": self.tempFile})
		await browser.close()

if __name__ == "__main__":
	win = visual.Window([800, 600], units="pix", monitor='testMonitor')
	stim = HyperTextStim(win, text=text, css="text-align: justify; font-size: 3.2mm; ", size=[700, 560])

	while not event.getKeys():
		stim.draw()
		win.flip()
