# Jellyfish

Jellyfish is an AI for [Piskvork gomoku manager](http://gomocup.org/download-gomocup-manager/) used in [Gomocup AI tournament](https://gomocup.org/).

Modified Alpha-beta pruned Minimax is implemented as main algorithm in `agent.py`.

The `pisqpipe.py` file is basically the "Python copy" of [C++ template](http://petr.lastovicka.sweb.cz/skel_cpp.zip) written by [Petr Lastovicka](http://petr.lastovicka.sweb.cz/indexEN.html).

## Build

Please note that the Piskvork manager is a Windows application and currently supports only Windows compatible `.exe` files (furthermore whose name starts with `pbrain-` prefix).

Run the following command to build `pbrain-jellyfish.exe`:

```powershell
$ python build.py
```
