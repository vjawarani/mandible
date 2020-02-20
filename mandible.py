import os
import json
import click
from pyfiglet import Figlet

firstStart = True

def remove(path, ext):
	removed=0
	try:
		ospath = os.listdir("path")
	except OSError:
		click.echo("double-check that your path exists and is a folder")
		pass
	for f in ospath:
		removed+=1
		if f.endswith(".ext"):
			os.remove(f)
			
	click.echo("removed %d '.%s' file" + ("" if removed==1 else "s") % (removed, ext), nl=False)
	click.echo(" from your %s folder!" % (path))


@click.command()
def defaultrm():
	folder = json.load("pref.json").default.defFolder
	ext = json.load("pref.json").default.defExt
	remove(folder, ext)

@click.command()
@click.option("-p", "--preset", "presnum", prompt="which preset would you like to use? ")
def presetrm():
	if presnum < 1 or presnum > 4:
		click.echo("make sure that the value you enter is 1, 2, 3, or 4")
	presetrm()
	folder = json.load("pref.json").presets.presnum.defFolder
	ext = json.load("pref.json").presets.presnum.defExt
	remove(folder, ext)

@click.command()
@click.arguments("-f", , "--fold-ext", nargs=2, prompt="enter a path to a folder and extension \n ex: \Users\usr\Downloads\ .dmg")
def foldextrm():
	folder = fold_ext
	ext = fold_ext
	remove(folder, ext)

@click.command()
@click.option("-sp", "--set_preset", nargs=2, prompt="enter a path to a folder and extension \n ex: \Users\usr\Downloads\ .dmg")
def setpreset():
	with open("pref.json", "r") as rw_file:
    	data = json.load(rw_file)

	







if __name__ == '__main__':
    f = Figlet(font='doom')
    print(f.renderText('Mandible'))