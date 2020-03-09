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
@click.option("-p", "--preset", "presnum", help="which preset would you like to use? ")
def presetrm(presnum):
    if presnum < 1 or presnum > 4:
        click.echo("make sure that the value you enter is 1, 2, 3, or 4")
        return
    folder = json.load("pref.json").presets.presnum.defFolder
    ext = json.load("pref.json").presets.presnum.defExt
    remove(folder, ext)

@click.command()
@click.argument("folder", type=click.Path(exists=True))
@click.argument("extension")
@click.option("-sp", "--set-preset", "preset", type=click.IntRange(1, 4))
def foldextrm(folder, extension, preset):
    if (preset):
        with open("pref.json") as f:
            data = f.read()
        d = json.loads(data)
        d["presets"][str(preset)]["defExt"]=extension
        d["presets"][str(preset)]["defFolder"]=folder
        with open("pref.json", 'w') as f:
            f.write(json.dumps(d))
    remove(folder, extension)

    







if __name__ == '__main__':
    f = Figlet(font='doom')
    print(f.renderText('Mandible'))