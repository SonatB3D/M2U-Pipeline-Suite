M2U PIPELINE SUITE
Maya to Unreal Static Mesh Preflight, Prep, Validation and Export Toolkit

Public Release README


============================================================
1. OVERVIEW
============================================================

M2U Pipeline Suite is a professional Autodesk Maya toolset designed to prepare
mesh assets before they are imported into Unreal Engine.

It is not just an FBX exporter. It is a complete Maya-to-Unreal preflight system
that helps artists, technical artists and asset creators analyze, clean, validate,
document and export game-ready static mesh assets.

The tool is built around a practical production workflow:

    Analyze Selected Assets
    Apply Safe Fixes
    Revalidate
    Export FBX + Reports

M2U Pipeline Suite focuses on common issues that appear when moving assets from
Maya to Unreal Engine, including:

    Naming problems
    Missing or incorrect prefixes
    Unfrozen transforms
    Construction history
    Incorrect pivots
    Grid alignment problems
    Incorrect dimensions
    Missing UCX collision
    UCX collision naming mismatches
    Material slot naming issues
    LOD readiness issues
    UV readiness issues
    Socket / locator readiness issues
    Export documentation and QA reporting

The goal is to reduce manual cleanup work, prevent avoidable Unreal import
problems and make the asset export process feel like a clean studio pipeline.


============================================================
2. KEY FEATURES
============================================================

M2U Pipeline Suite includes the following major systems:

    Modern PySide-based Maya interface
    Dashboard status cards
    Wizard-style workflow
    User-friendly presets
    Safe fix system
    M2U asset readiness score
    Naming validation
    Prefix validation
    Automatic base mesh prefix fix
    UCX collision matching
    UCX required / optional / forbidden modes
    UCX prefix sync when base meshes are renamed
    UCX export inclusion
    Export-time UCX recheck
    Geometry validation
    Freeze transform validation
    Construction history validation
    Polycount validation
    Dimension validation
    Pivot validation
    Grid readiness validation
    Pivot preview locator
    Simple box UCX creation
    UCX preview colorizing
    LOD readiness check
    Material slot readiness check
    UV readiness check
    Socket / locator readiness check
    Nanite-oriented preflight preset
    JSON report export
    HTML QA report export
    Unreal Engine import script generation
    Shelf installer for Maya
    Custom shelf icon support


============================================================
3. SUPPORTED SOFTWARE
============================================================

Target Maya version:

    Autodesk Maya 2024 and newer

The interface is designed with PySide compatibility handling for modern Maya
versions. Maya 2024 commonly uses PySide2. Newer Maya versions may use PySide6.
The tool includes fallback handling for both.

Required Maya components:

    Python 3 environment
    maya.cmds
    Maya FBX plug-in for FBX export

Recommended Unreal Engine usage:

    Unreal Engine 5.x
    Python Editor Script Plugin enabled if using the generated Unreal import script

The generated Unreal import script is not executed inside Maya. It is intended
to be run inside Unreal Editor.


============================================================
4. PACKAGE CONTENTS
============================================================

A typical public release package includes:

    m2u_pipeline_suite_v1_0.py
        Main Maya tool.

    M2U Pipeline Suite.py
        Simple launcher script for Maya.

    M2U_Pipeline_Suite_v1_0_8_Easy_Installer.py
        Easy installer. It lets the user choose an installation folder and
        creates or updates the Maya shelf button.

    reinstall_m2u_pipeline_suite_shelf_button.py
        Reinstalls the Maya shelf button without reinstalling the whole tool.

    m2u_pipeline_suite_icon.png
        Shelf button icon.

    M2U_Pipeline_Suite_README.txt
        General documentation.

    M2U_Pipeline_Suite_FUNCTIONS.txt
        Detailed function reference.


============================================================
5. INSTALLATION
============================================================

The recommended installation method is the Easy Installer.

Steps:

    1. Extract the package to any temporary location.

    2. Open Autodesk Maya.

    3. Open:
           Windows > General Editors > Script Editor

    4. Switch to the Python tab.

    5. Open or drag the Easy Installer script into the Python tab:
           M2U_Pipeline_Suite_v1_0_8_Easy_Installer.py

    6. Run the script.

    7. Choose the folder where the tool should be installed.

    8. The installer copies the required files to the selected folder.

    9. The installer creates or updates the Maya shelf:
           M2U_Tools

    10. A shelf button named:
           M2U Pipeline Suite
        will be added to the shelf.

After installation, users do not need to run the installer again. The tool can be
launched from the M2U_Tools shelf.


============================================================
6. LAUNCHING THE TOOL
============================================================

After installation, launch the tool from:

    Maya Shelf > M2U_Tools > M2U Pipeline Suite

If the shelf button is removed or Maya preferences are reset, run:

    reinstall_m2u_pipeline_suite_shelf_button.py

This will recreate the shelf button without reinstalling the whole package.


============================================================
7. QUICK START WORKFLOW
============================================================

Basic recommended workflow:

    1. Select one or more static mesh assets in Maya.

    2. Open M2U Pipeline Suite.

    3. Choose a preset.

    4. Click:
           Analyze Selected Assets

    5. Review the dashboard, asset table and detail panel.

    6. Click:
           Apply Safe Fixes

    7. Click:
           Revalidate

    8. Click:
           Export FBX + Reports

    9. Open the generated HTML report to review the final export.

    10. If needed, run the generated Unreal import script inside Unreal Editor.

This workflow is designed to keep the user in control while still automating
repetitive and safe cleanup tasks.


============================================================
8. WIZARD FLOW BUTTONS
============================================================

Analyze Selected Assets

    Scans the currently selected Maya transforms and validates them against the
    active preset and current UI settings.

    It checks naming, geometry, transforms, history, pivot, grid, dimensions,
    collision, material slots, UV readiness, LOD readiness and socket readiness.

Apply Safe Fixes

    Applies enabled safe fixes to the selected assets.

    Depending on the selected options, it can:
        Create backup duplicates
        Hide backups
        Sanitize names
        Add missing prefixes
        Rename related UCX collision meshes
        Freeze transforms
        Delete construction history
        Move pivots
        Snap assets to grid
        Unlock transform attributes
        Make selected assets visible

    After the fix operation, the tool restores the selection to the actual
    processed base meshes, not to backup objects.

Revalidate

    Runs analysis again on the current selected assets. This is useful after
    applying safe fixes.

Export FBX + Reports

    Exports ready assets to FBX and generates optional reports.

    Depending on the enabled export options, it can create:
        FBX files
        JSON report
        HTML QA report
        Unreal import script

Clear Results

    Clears the tool UI results, dashboard data, report paths and internal
    analysis summary.

    It does not modify the Maya scene.

Reset to Defaults

    Resets the interface to user-friendly default settings.

    It does not modify the Maya scene.

    Defaults are designed around a practical Marketplace Static Mesh style
    workflow with safe cleanup enabled and strict destructive actions avoided.


============================================================
9. PRESETS
============================================================

M2U Pipeline Suite includes several presets to quickly configure the tool for
different production scenarios.

Marketplace Static Mesh

    General-purpose static mesh export preset.
    Recommended for props, furniture, environment pieces and marketplace assets.

    Typical behavior:
        Required prefix: SM_
        UCX collision optional
        Freeze transform required
        Clean history warning
        Pivot check enabled
        Grid warning enabled
        Reports enabled

Modular Wall Kit

    Designed for modular environment assets.

    Typical behavior:
        Strict grid readiness
        Dimension checks enabled
        Pivot suitable for modular placement
        Stronger warnings for non-grid-aligned assets

Furniture / Prop

    Designed for standalone props and furniture assets.

    Typical behavior:
        Pivot commonly set to bottom center
        UCX optional
        Material and UV readiness checks enabled
        Friendly polycount threshold

Collision Strict

    Designed for assets where custom collision is mandatory.

    Typical behavior:
        UCX required
        Missing UCX can block export
        UCX validation is stricter
        Export includes matching UCX meshes

Nanite-Oriented Preflight

    Designed for high-detail static meshes where Nanite-oriented review is
    useful.

    Typical behavior:
        Higher polycount tolerance
        Collision remains checked
        LOD readiness may be less strict
        Focuses on export readiness rather than classic low-poly validation

Presets are starting points. Users can change settings manually after selecting
a preset.


============================================================
10. NAMING AND PREFIX SYSTEM
============================================================

The tool can validate and fix asset names.

Common expected static mesh prefix:

    SM_

Example valid names:

    SM_Table_01
    SM_Chair_01
    SM_Wall_400x300

Custom prefixes are also supported.

Example:

    ZM_Table_01

If Add Prefix If Missing is enabled, the tool can rename:

    Table_01

to:

    SM_Table_01

or to another custom prefix chosen by the user.

The naming system can also sanitize invalid characters for safer file and object
names.


============================================================
11. UCX COLLISION SYSTEM
============================================================

M2U Pipeline Suite includes a UCX collision workflow for Unreal-oriented static
mesh export.

Recommended Unreal-style naming:

    Base mesh:
        SM_Table_01

    UCX collision:
        UCX_SM_Table_01
        UCX_SM_Table_01_01
        UCX_SM_Table_01_02

The tool can detect UCX collision meshes that match the selected base asset.

Collision requirement modes:

    Off
        Collision checks are ignored.

    UCX required
        A matching UCX collision mesh is required.
        If no matching UCX is found, the asset can be blocked from export.

    UCX optional
        Matching UCX collision is allowed but not required.
        If UCX exists, it can be validated and included in export.

    No custom collision allowed
        UCX collision is not allowed.
        If UCX meshes are found, the tool can warn or block depending on severity.

UCX match modes:

    Base asset name
        The tool expects UCX names to match the base asset name.

        Example:
            SM_Table_01
            UCX_SM_Table_01

    Exact custom target name
        The user can specify a custom target name for collision matching.

        This is useful for special naming workflows, but automatic UCX prefix
        sync is intentionally not applied in this mode to avoid unwanted renames.


============================================================
12. UCX PREFIX SYNC
============================================================

UCX Prefix Sync is one of the key workflow features.

When a base mesh receives a prefix during Safe Fix, the tool can also rename
matching UCX collision meshes to match the new base mesh name.

Example before Safe Fix:

    Chair_01
    UCX_Chair_01
    UCX_Chair_01_02

Required prefix:

    SM_

After Safe Fix:

    SM_Chair_01
    UCX_SM_Chair_01
    UCX_SM_Chair_01_02

The tool preserves multipart UCX suffixes.

Example:

    UCX_Chair_01_01
    UCX_Chair_01_02
    UCX_Chair_01_03

becomes:

    UCX_SM_Chair_01_01
    UCX_SM_Chair_01_02
    UCX_SM_Chair_01_03

This feature is designed to prevent a common workflow problem where the base
mesh is renamed but the collision meshes keep the old names.


============================================================
13. EXPORT-TIME UCX RECHECK
============================================================

Before exporting, the tool rechecks matching UCX collision meshes.

This is important because the scene may have changed after the original analysis.
For example, the user may have renamed, created or fixed collision after the
first analysis.

If UCX Required is enabled and no matching UCX is found at export time, the tool
can prevent exporting the base mesh alone. This helps avoid accidental Unreal
imports without required custom collision.


============================================================
14. SAFE FIX SYSTEM
============================================================

The Safe Fix system is designed to automate common cleanup operations while
protecting the user's original work.

Safe fix options can include:

    Duplicate Backup Before Fix
        Creates backup duplicates before modifying assets.

    Hide Backups
        Hides backup duplicates to keep the scene clean.

    Add Prefix If Missing
        Adds the required prefix to base meshes.

    Sanitize Asset Names
        Replaces unsafe characters with underscores.

    Sync UCX Names To Base Prefix When UCX Required
        Renames matching UCX collision meshes after a base mesh rename.

    Freeze Transform
        Freezes transforms on selected assets.

    Delete Construction History
        Deletes construction history.

    Move Pivot To Target
        Moves pivot to the selected target position.

    Snap Bounds Min To Grid
        Moves the asset so its minimum bounds align to the grid.

    Snap Pivot To Grid
        Moves the asset so its pivot aligns to the grid.

    Unlock Transform Attributes During Fix
        Unlocks locked transform attributes if enabled.

    Make Selected Assets Visible During Fix
        Makes selected assets visible if enabled.

Safe Fix does not automatically resize geometry unless a specific grid movement
option is enabled. It is intended to prepare assets, not redesign them.


============================================================
15. PIVOT SYSTEM
============================================================

The pivot system can analyze and fix pivot placement.

Supported pivot targets include:

    Center
    Bottom Center
    Bottom Front Center
    Bottom Back Center
    Bottom Left Center
    Bottom Right Center
    Bottom Front Left
    Bottom Front Right
    Bottom Back Left
    Bottom Back Right
    Front Center
    Back Center
    Left Center
    Right Center
    Top Center
    Top Front Center
    Top Back Center
    Top Left Center
    Top Right Center
    Top Front Left
    Top Front Right
    Top Back Left
    Top Back Right

Maya Y is treated as the up / height axis.

The Front Axis setting controls how "front", "back", "left" and "right" are
interpreted.

Supported front axes:

    +X
    -X
    +Z
    -Z

Pivot Preview

    The tool can create temporary preview locators to show where the target pivot
    should be.

Delete Pivot Preview Locators

    Removes temporary M2U pivot preview locators from the scene.


============================================================
16. GRID READINESS
============================================================

Grid readiness helps detect assets that may not work well in modular workflows.

The tool can check:

    Bounds alignment
    Size multiples
    Pivot alignment
    Grid step compliance

Example:

    Grid Step: 10 cm

An asset with width:

    400 cm

passes the size multiple check.

An asset with width:

    397.83 cm

fails or warns because it is not a clean multiple of the grid step.

Grid-related checks are especially useful for modular wall kits, floors, trims,
doors, windows and architectural assets.


============================================================
17. DIMENSION VALIDATION
============================================================

Dimension validation compares the asset bounding box size to expected dimensions.

Configurable values:

    Expected Width
    Expected Height
    Expected Depth
    Tolerance

Example:

    Expected Width: 100 cm
    Expected Height: 300 cm
    Expected Depth: 20 cm
    Tolerance: 0.5 cm

If the asset dimensions are outside tolerance, the tool can warn or block export
depending on severity.

Dimension validation can be disabled for freeform props.


============================================================
18. GEOMETRY VALIDATION
============================================================

Geometry validation includes:

    Polycount check
    Freeze transform check
    Construction history check
    Zero thickness check
    Visibility check
    Locked transform attribute check

Polycount

    Compares the asset face count against the maximum polycount setting.

Freeze Transform

    Detects non-zero translate / rotate or non-one scale values.

Construction History

    Detects construction history nodes that may be unwanted before export.

Zero Thickness

    Detects bounding box axes that are near zero.

Visibility

    Detects hidden objects or hidden parent hierarchy.

Locked Attributes

    Detects locked translate, rotate, scale or visibility attributes.


============================================================
19. MATERIAL SLOT READINESS
============================================================

Material Slot Readiness checks whether assigned material names follow a clean
Unreal-oriented naming convention.

Accepted common prefixes include:

    M_
    MI_
    MAT_

Example valid names:

    M_Wood
    M_Metal
    MAT_Chair_Fabric
    MI_Table_Surface

Example warning:

    standardSurface1

This often means the asset still uses a default Maya material name.

The tool does not create Unreal materials. It only checks material slot naming
readiness in Maya.


============================================================
20. UV READINESS
============================================================

UV Readiness checks basic UV export preparedness.

The tool can check:

    UV set existence
    UV coordinate count
    Lightmap UV requirement
    Sampled UV values outside the 0-1 range

This is a readiness check, not a full UV packing or full overlap detection
system.

It does not replace dedicated UV tools, but it helps detect common missing or
obvious UV issues before export.


============================================================
21. LOD READINESS
============================================================

LOD Readiness checks LOD-style naming and basic LOD logic.

It can help review:

    LOD0 / LOD1 / LOD2 naming
    Polycount reduction between LOD levels
    Pivot consistency
    Bounding box consistency

The tool does not automatically configure Unreal LOD settings. It is a Maya-side
preflight check for assets that use LOD naming conventions.


============================================================
22. SOCKET / LOCATOR READINESS
============================================================

Socket / Locator Readiness checks locator-style helper objects intended for
attachment points or Unreal-related workflows.

Typical names:

    SOCKET_Handle
    SOCKET_VFX_Smoke
    Socket_DoorPivot

The tool can identify socket-like locators and check basic readiness issues.

It does not guarantee automatic Unreal socket creation by itself. Socket import
behavior may require an Unreal-side setup or an extended Unreal import script.


============================================================
23. COLLISION PREVIEW TOOLS
============================================================

Select Asset + UCX

    Selects the base asset and its matching UCX collision meshes.

Isolate Asset + UCX

    Attempts to isolate the base asset and matching UCX meshes in the active
    Maya viewport.

Colorize UCX Preview

    Assigns preview material to matching UCX collision meshes to make them easier
    to inspect.

Reset UCX Preview Materials

    Restores UCX preview material assignments from the current Maya session.

    Note:
        This restore is session-based. If Maya is closed, the temporary restore
        memory is lost.


============================================================
24. SIMPLE BOX UCX CREATION
============================================================

The tool can create a simple box-shaped UCX collision mesh based on the selected
asset bounding box.

Example:

    Base mesh:
        SM_Table_01

    Created collision:
        UCX_SM_Table_01

This is useful for simple props where a box collision is enough.

For complex collision, artists should still create proper custom collision
meshes manually.


============================================================
25. REPORTING SYSTEM
============================================================

M2U Pipeline Suite can generate professional export reports.

JSON Report

    Machine-readable report containing asset results, checks, warnings, blocking
    issues, export status and settings.

HTML QA Report

    Human-readable report for review, delivery, documentation or support.

The HTML report can include:

    Summary
    Asset list
    M2U score
    Validation status
    Naming result
    Geometry result
    Pivot result
    Grid result
    Collision result
    UCX matches
    Collision target candidates
    Readiness checks
    Export status
    Warnings
    Blocking issues

Reports are designed to make the pipeline more transparent and professional.


============================================================
26. UNREAL IMPORT SCRIPT
============================================================

The tool can generate an Unreal Python import script after FBX export.

Generated file:

    M2U_Unreal_Import_Assets.py

This script is intended to be run inside Unreal Editor, not inside Maya.

Basic Unreal usage:

    1. Open the Unreal project.

    2. Enable Python Editor Script Plugin if needed.

    3. Open:
           Window > Output Log

    4. Switch the command input to Python mode.

    5. Run:
           exec(open("PATH_TO_SCRIPT").read())

The generated script imports exported FBX files into the configured Unreal
destination path.

Default destination path may be:

    /Game/M2U_Imported

Users can edit the generated script to change the destination path.


============================================================
27. SEVERITY SYSTEM
============================================================

Many checks support severity levels.

Off

    The check is ignored or does not affect the result.

Warning

    The issue appears as a warning.
    The asset may still be exportable depending on export settings.

Blocking

    The issue becomes a blocking problem.
    The asset should not export unless blocking export is disabled or the issue
    is fixed.

This allows the same tool to support both strict studio validation and flexible
artist-friendly workflows.


============================================================
28. EXPORT BEHAVIOR
============================================================

Export behavior can be configured.

Common options:

    Export Ready Assets
        Exports assets that pass validation.

    Export Warning Assets
        Allows assets with warnings to export.

    Skip Blocked Assets
        Prevents blocked assets from exporting.

    Write JSON Report
        Creates JSON report.

    Write HTML Report
        Creates HTML QA report.

    Generate Unreal Import Script
        Creates Unreal Python import script.

    Triangulate FBX Export
        Triangulates geometry during export if enabled.

UCX Export Inclusion

    When matching UCX meshes are found, the tool includes them in the FBX export
    selection with the base mesh.


============================================================
29. RECOMMENDED NAMING CONVENTIONS
============================================================

Static meshes:

    SM_Table_01
    SM_Chair_01
    SM_Wall_400x300

UCX collision:

    UCX_SM_Table_01
    UCX_SM_Table_01_01
    UCX_SM_Table_01_02

Materials:

    M_Wood
    M_Metal
    MAT_Fabric
    MI_Plastic_Black

LOD meshes:

    SM_Table_01_LOD0
    SM_Table_01_LOD1
    SM_Table_01_LOD2

Socket / locator helpers:

    SOCKET_Handle
    SOCKET_VFX_Smoke
    SOCKET_DoorPivot


============================================================
30. WHAT THE TOOL DOES NOT DO
============================================================

M2U Pipeline Suite is a Maya-side preparation, validation and export assistant.

It does not:

    Replace full manual art review
    Guarantee perfect UV packing
    Perform full UV overlap detection
    Automatically create complex collision for every asset
    Automatically create Unreal materials
    Automatically configure every Unreal static mesh setting
    Replace Unreal Editor validation
    Permanently remember preview material states after Maya is closed

Some systems are intentionally readiness checks rather than full automation.
This keeps the tool safe, predictable and suitable for artist-controlled
workflows.


============================================================
31. BEST PRACTICES
============================================================

Recommended usage:

    Use clear asset names before export.
    Keep base mesh and UCX collision naming consistent.
    Use presets as a starting point.
    Analyze before fixing.
    Review the Fix Plan before applying fixes.
    Revalidate after fixes.
    Check the HTML report after export.
    Use UCX Required for assets that must have custom collision.
    Use UCX Optional for general props where collision may not always be needed.
    Use Modular presets for grid-based kits.
    Use Pivot Preview when preparing placement-critical assets.
    Keep backups enabled during cleanup.


============================================================
32. TROUBLESHOOTING
============================================================

The tool does not open

    Make sure the files were installed correctly.
    Reinstall the shelf button.
    Confirm the script is being run in Maya Python, not MEL.

FBX export fails

    Make sure the Maya FBX plug-in is available.
    Check that the export folder is writable.
    Check the HTML/JSON report if it was generated.
    Revalidate the asset and inspect blocking issues.

UCX is not found

    Check the UCX name.
    Make sure the UCX mesh is a transform with mesh shape.
    Make sure it follows the expected naming convention.
    Re-run Analyze Selected Assets.
    If the base mesh was renamed, use Apply Safe Fixes with UCX Prefix Sync
    enabled.

UCX does not export

    Make sure Collision Requirement is not Off.
    Make sure the UCX mesh matches the base mesh name.
    Make sure the asset is not blocked.
    Revalidate before export.

Material naming fails

    Rename default Maya materials such as standardSurface1 to a cleaner name.

    Example:
        M_Table_Wood
        MAT_Table_Surface

Pivot result is wrong

    Check Front Axis.
    Maya Y is treated as height/up.
    Use Pivot Preview to inspect the target pivot position.

Shelf icon is missing

    Make sure m2u_pipeline_suite_icon.png is installed beside the tool files.
    Reinstall the shelf button.


============================================================
33. PUBLIC RELEASE NOTES
============================================================

This public version is intended as a complete first release of the M2U Pipeline
Suite toolset.

It includes the major systems needed for a professional Maya-to-Unreal static
mesh export workflow:

    Preparation
    Validation
    UCX matching
    UCX prefix sync
    Safe fixes
    Export
    Reporting
    Unreal import script generation

It is recommended to test the tool on duplicate scenes or non-critical assets
before using it in production.


============================================================
34. LICENSE / USAGE NOTE
============================================================

This README describes the public release package of M2U Pipeline Suite.

Studios, artists and marketplace creators should review their own project
requirements before relying on any automated export tool in production.

Always keep backups of important Maya scenes.
