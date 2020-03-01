import maya.cmds as cmds
import maya.OpenMaya as om
import random
#----------------------------------------------------------------------
tx = 5
tz = 5
ty = 5
#----------------------------------------------------------------------
sx = 2
sy = 2
sz = 2
#----------------------------------------------------------------------
def window_gui_creation():
    window_name = "Speed_GUI"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    window = cmds.window(window_name)
    cmds.showWindow(window)
    scroll = cmds.scrollLayout(verticalScrollBarAlwaysVisible=True)
#----------------------------------------------------------------------

#----------------------------------------------------------------------
def creation_function(*args):
    poly_number = 0
    radio = cmds.radioCollection("objectType", query=True, select=True)
    mode = cmds.radioButton(radio, query=True, label=True)
    numobjects = cmds.intField("Numofobjects", query=True, value=True)
    print(mode, numobjects)
    if mode == "Cube":
        for i in range (numobjects):
            cmds.polyCube(name="{}_0{}".format("cube", str(poly_number)))
            poly_number += 1
    elif mode == "Sphere":
        for i in range (numobjects):
            cmds.polySphere(name="{}_0{}".format("sphere", str(poly_number)))
            poly_number += 1
    elif mode == "Cylinder":
        for i in range (numobjects):
            cmds.polyCylinder(name="{}_0{}".format("cylinder", str(poly_number)))
            poly_number += 1
#----------------------------------------------------------------------
def rename_collection_function():
    poly_number = 0
    selection = cmds.ls(sl=True)
    new_name = cmds.textField("name", query=True, text=True)
    for i in selection:
        cmds.rename(i, "{}_0{}".format(new_name, str(poly_number)))
        poly_number += 1
#----------------------------------------------------------------------
def rename_single_obj_function():
    selection = cmds.ls(sl=True)
    N_name = cmds.textField("name", query=True, text=True)
    for i in selection:
        cmds.rename(i, "{}".format(N_name))
#----------------------------------------------------------------------
def randomize_function_translate():
    poly_number = 0
    selection = cmds.ls(sl=True)
    for i in range(len(selection)):
        cmds.setAttr("{}.t".format(selection[poly_number]), random.randint(-tx-i, tx+i), random.randint(-ty-i, ty+i), random.randint(-tz-i, tz+i), type="double3")
        poly_number += 1
#----------------------------------------------------------------------
def randomize_function_scale():
    poly_number = 0
    selection = cmds.ls(sl=True)
    for i in range(len(selection)):
        cmds.setAttr("{}.s".format(selection[poly_number]), random.randint(1, sx+i), random.randint(1, sy+i), random.randint(1, sz+i), type="double3")
        poly_number += 1
#----------------------------------------------------------------------
def select_all():
    cmds.SelectAll()
#----------------------------------------------------------------------
def deselect_all():
    cmds.select(clear=True)
#----------------------------------------------------------------------
def group():
    cmds.SelectAll()
    selection = cmds.ls(sl=True)
    cmds.group(selection)
#----------------------------------------------------------------------
def ungroup():
    selection = cmds.ls(sl=True)
    cmds.ungroup(selection)
#----------------------------------------------------------------------
def delete_selected():
    selection = cmds.ls(sl=True)
    cmds.delete(selection)
#----------------------------------------------------------------------
def hide_cams():
    cmds.HideCameras()
#----------------------------------------------------------------------
def hide_selected():
    selection = cmds.ls(sl=True)
    for i in selection:
        cmds.hide(i)
#----------------------------------------------------------------------
def show_all():
    cmds.ShowAll()
#----------------------------------------------------------------------
def delete_history():
    cmds.DeleteHistory()
#----------------------------------------------------------------------
def delete_all_history():
    cmds.DeleteAllHistory()
#----------------------------------------------------------------------
def gui_layout():
    column = cmds.columnLayout()
    cmds.frameLayout("Choose_obj_to_create")
    cmds.columnLayout()
    cmds.radioCollection("objectType")
    cmds.radioButton(label="Cube", select=True)
    cmds.radioButton(label="Sphere")
    cmds.radioButton(label="Cylinder")
#----------------------------------------------------------------------
    cmds.frameLayout("Choose_num_of_objs")
    cmds.intField("Numofobjects", value=3)
#----------------------------------------------------------------------
    cmds.setParent(column)
    cmds.frameLayout(label="Start_Your_Test")
    cmds.button(label="Create", actOnPress=True, command="creation_function()")
#----------------------------------------------------------------------
    cmds.button(label="Select_All", actOnPress=True, command="select_all()")
    cmds.button(label="Deselect_All", actOnPress=True, command="deselect_all()")
#----------------------------------------------------------------------
    cmds.frameLayout("Type_Name")
    cmds.textField("name", insertText="")
    cmds.button(label="Rename_single_obj", actOnPress=True, command="rename_single_obj_function()")
    cmds.button(label="Rename_Collection", actOnPress=True, command="rename_collection_function()")
#----------------------------------------------------------------------
    cmds.button(label="Randomize_translation", actOnPress=True, command="randomize_function_translate()")
    cmds.button(label="Randomize_scale", actOnPress=True, command="randomize_function_scale()")
#----------------------------------------------------------------------
    cmds.button(label="Group", actOnPress=True, command="group()")
    cmds.button(label="Un_Group", actOnPress=True, command="ungroup()")
#----------------------------------------------------------------------
    cmds.button(label="Delete", actOnPress=True, command="delete_selected()")
    cmds.button(label="HideCameras", actOnPress=True, command="hide_cams()")
    cmds.button(label="HideSelected", actOnPress=True, command="hide_selected()")
    cmds.button(label="ShowAll", actOnPress=True, command="show_all()")
    cmds.button(label="Delete_history", actOnPress=True, command="delete_history()")
    cmds.button(label="Delete_all_history", actOnPress=True, command="delete_all_history()")
#----------------------------------------------------------------------
window_gui_creation()
#----------------------------------------------------------------------
gui_layout()
#----------------------------------------------------------------------
