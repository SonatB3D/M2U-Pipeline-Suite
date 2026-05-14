# -*- coding: utf-8 -*-
"""Reinstall/update the M2U Pipeline Suite shelf button."""
from __future__ import print_function
import os
import sys

SHELF_NAME = "M2U_Tools"
BUTTON_LABEL = "M2U Pipeline Suite"
BUTTON_ANNOTATION_MARKER = "M2U_PIPELINE_SUITE_BUTTON"
ICON_NAME = "m2u_pipeline_suite_icon.png"
VERSION_LABEL = "v1.0.8"


def _build_shelf_command(install_dir):
    safe_dir = install_dir.replace("\\", "/").replace("'", "\\'")
    return "import sys, importlib\ntool_dir = r'%s'\nif tool_dir not in sys.path:\n    sys.path.insert(0, tool_dir)\nimport m2u_pipeline_suite_v1_0\ntry:\n    importlib.reload(m2u_pipeline_suite_v1_0)\nexcept Exception:\n    pass\nm2u_pipeline_suite_v1_0.show()\n" % safe_dir


def install():
    import maya.cmds as cmds
    import maya.mel as mel
    install_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        shelf_top = mel.eval("$tmp=$gShelfTopLevel")
    except Exception:
        shelf_top = None
    if not cmds.shelfLayout(SHELF_NAME, exists=True):
        if shelf_top:
            cmds.shelfLayout(SHELF_NAME, parent=shelf_top)
        else:
            cmds.shelfLayout(SHELF_NAME)
    for child in cmds.shelfLayout(SHELF_NAME, q=True, childArray=True) or []:
        try:
            label = cmds.shelfButton(child, q=True, label=True)
            ann = cmds.shelfButton(child, q=True, annotation=True) or ""
            if label == BUTTON_LABEL or BUTTON_ANNOTATION_MARKER in ann:
                cmds.deleteUI(child)
        except Exception:
            pass
    icon_path = os.path.join(install_dir, ICON_NAME)
    cmds.shelfButton(
        parent=SHELF_NAME,
        label=BUTTON_LABEL,
        annotation=BUTTON_ANNOTATION_MARKER + " - Open M2U Pipeline Suite " + VERSION_LABEL,
        command=_build_shelf_command(install_dir),
        sourceType="python",
        image1=icon_path if os.path.isfile(icon_path) else "commandButton.png",
        imageOverlayLabel="M2U",
        overlayLabelColor=(1.0, 1.0, 1.0),
        overlayLabelBackColor=(0.05, 0.08, 0.12, 0.75),
    )
    try:
        mel.eval('saveAllShelves $gShelfTopLevel;')
    except Exception:
        pass
    print("M2U Pipeline Suite shelf button installed/updated: %s" % SHELF_NAME)


install()
