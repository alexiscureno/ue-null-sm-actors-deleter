# ue-null-sm-actors-deteler
This script is a Python module that uses the Unreal Engine Python API to delete all Static Mesh Actors in the currently loaded level that have an invalid mesh component.

# Requirements
* Unreal Engine 4.26
* Python 3.7
* The Unreal Engine Python API

# Installation
1. Clone this repository or download the ZIP archive and extract its contents.
2. Copy and paste it into your Unreal Engine projects script file.
3. In  Unreal Engine, go to the **File** menu, select **Execute Python Script**, and navigate to the ```invalid_mesh_actor_deleter.py``` file and run it.


# Usage
1. Open the Unreal Editor
2. Go to the **File** menu, select **Execute Python Script**, and navigate to the ```invalid_mesh_actor_deleter.py``` file and run it.
3. The script will automatically delete all Static Mesh Actors with an invalid mesh component


# Notes
* This script only works with Static Mesh Actors, not other types of Actors
* This script does not prompt for confirmation before deleting Actors, so use with caution
* This script can be modified to change the conditions under which Actors are deleted by editing the ```is_valid_actor``` variable in the script.
