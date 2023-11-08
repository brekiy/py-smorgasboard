import bpy
import os
from itertools import chain, combinations, product

# This script is meant to automate exporting combined objects from a list of collections in your workspace.

# Main collection
main_col = 'main'
# Subcollection addons, in the format of name - combo_type: see powerset()
sub_col = [('hats', 'single'), ('shirts', 'singleNoEmpty')]
# This marks the collection of objects you always want selected.
always_on = 'Base'
# Prefix the filename and mkdir the folder if it doesn't exist
prefix = 'filename_prefix'
folder = 'folder_name'

# Get the current path and make a new folder for the exported meshes
path = bpy.path.abspath(f'//stlexport/{folder}/')

# If the path doesn't exist, create the folder
if not os.path.exists(path):
    os.makedirs(path)

def powerset(iterable, combo_type = 'full'):
    'powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'
    s = list(iterable)
    match combo_type:
        case 'full':
            # full powerset
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
        case 'single':
            # picks anywhere from 0 to 1 elements
            return chain.from_iterable(combinations(s, r) for r in range(2)) 
        case 'singleNoEmpty':
            # picks 1 element
            return chain.from_iterable(combinations(s, r) for r in range(1, 2))

def selectBase():
    for ob in bpy.data.collections.get(always_on).objects:
        ob.select_set(True)

def processSubcollections():
    """Calculates the desired object combinations per collection."""
    for col in sub_col:
        objset = list(powerset(bpy.data.collections.get(col[0]).objects, col[1]))
        subcolsets.append(objset)

def generateCombinations(args):
    combos = []
    for combination in product(*args):
        combos.append(combination)
    return combos
# return [x for x in product(*args)]

# Loop through the collection called 'Pieces', select the objects one by one, export them, and finally deselect them.
# You can have as many nested loops as you wish. If you wanted to generate all combinations of two collections for example,
# you would simply add a second loop,
#	for ob2 in bpy.data.collections.get('Pieces2').objects:
# select the object, add the name in the path variable so it won't get overwritten, and finally deselect the second object as well.
# And following that pattern you can add as many loops as you wish.

idx1 = 1
subcolsets = []

processSubcollections()
collections = [bpy.data.collections.get(main_col).objects]
for i in subcolsets:
    collections.append(i)
combos = generateCombinations(collections)
for combo in combos:
    bpy.ops.object.select_all(action='DESELECT')
    selectBase()
    for comp in combo:
        if type(comp) is tuple:
            for j in comp:
                j.select_set(True)
        else:
            comp.select_set(True)
    
    filename = f'{prefix}_{idx1}'
    idx1 += 1
    # Set the filepath and name
    fPath = str(path + filename + '.stl')
    #Export the selected meshes as STL
    bpy.ops.export_mesh.stl(filepath=fPath, use_selection=True,use_mesh_modifiers=False)

print('all done')