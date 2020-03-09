import os
import json
import click
#from pyfiglet import Figlet

class Config(object):
    def __init__(self):
        self.verbose=False

pass_config=click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option("--verbose", is_flag=True, help="More info - antonym of tl;dr")
@pass_config
def cli(config, verbose):
    #f = Figlet(font='doom')
    #click.echo(f.renderText('mandible'))
    config.verbose=verbose

def remove(path, ext, verbose):
    if(ext.startswith(".")):
        ext=ext[1:]
    removed=0
    path=os.path.join(path, '')
    try:
        osdir = os.listdir(path)
    except OSError:
        click.echo("Double-check that your path exists and is a folder")
        pass
    for f in osdir:
        if f.endswith("."+ext):
            removed+=1
            os.remove(path+f)
            if verbose:
                click.echo("removed {0}".format(f))
            
    theLetterS="" if removed==1 else "s"
    printStatement="Mandible removed %d .%s file%s from your %s folder!" % (removed, ext, theLetterS, path)        
    click.secho(printStatement, fg='cyan', bg="black")


@cli.command()
@pass_config
def defrm(config):
    """Removes files from folder according to default preset
    
    Set the default preset by running foldextrm with -sd as an option"""
    #folder = json.load("pref.json").default.defFolder
    #ext = json.load("pref.json").default.defExt
    with open("pref.json") as f:
        data = f.read()
    d = json.loads(data)
    folder=d["default"]["defFolder"]
    ext=d["default"]["defExt"]
    remove(folder, ext, config.verbose)

@cli.command()
@pass_config
@click.argument("preset", type=click.IntRange(1, 4))
def presetrm(config, preset):
    """Removes files using the folder and extension defined in the preset"""
    with open("pref.json") as f:
        data = f.read()
    d = json.loads(data)
    folder = d["presets"][str(preset)]["defFolder"]
    ext = d["presets"][str(preset)]["defExt"]
    if (folder is None) or (ext is None):
        click.echo("That preset has not been set yet")
        return
    remove(folder, ext, config.verbose)

@cli.command()
def printpresets():
    """Prints the set presets"""
    with open("pref.json") as f:
        data = f.read()
    d = json.loads(data)
    folder=d["default"]["defFolder"]
    ext=d["default"]["defExt"]
    click.echo("Default Preset is set to:\nfolder: %s\next:%s\n" % (folder, ext))
    for i in range(1,5):
        folder = d["presets"][str(i)]["defFolder"]
        ext = d["presets"][str(i)]["defExt"]
        if folder and ext:
            click.echo("Preset %d is set to:\nfolder: %s\next:%s\n" % (i, folder, ext))
        else:
            click.echo("Preset %d has not been set yet\n" % (i))

@cli.command()
@pass_config
@click.argument("folder", type=click.Path(exists=True))
@click.argument("extension")
@click.option("-sp", "--set-preset", "preset", type=click.IntRange(1, 4), help="set as preset 1-4")
@click.option("-sd", "--set-default", "default", is_flag=True, help="set as default folder and extension")
def foldextrm(config, folder, extension, preset, default):
    """Removes files from <folder> with <extension>"""
    if preset:
        with open("pref.json") as f:
            data = f.read()
        d = json.loads(data)
        d["presets"][str(preset)]["defExt"]=extension
        d["presets"][str(preset)]["defFolder"]=folder
        if default:
            d["default"]["defExt"]=extension
            d["default"]["defFolder"]=folder
            if config.verbose:
                click.echo("Set default!")
        with open("pref.json", 'w') as f:
            f.write(json.dumps(d))
        if config.verbose:
                click.echo("Set preset {0}!".format(preset))
    if default:
        with open("pref.json") as f:
            data = f.read()
        d = json.loads(data)
        d["default"]["defExt"]=extension
        d["default"]["defFolder"]=folder
        with open("pref.json", 'w') as f:
            f.write(json.dumps(d))
        if config.verbose:
                click.echo("Set default!")
        
    remove(folder, extension, config.verbose)

# if __name__ == '__main__':
#     f = Figlet(font='doom')
#     print(f.renderText('mandible'))