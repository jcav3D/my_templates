# Pull Request: Image Plane Generator – Arc and Grid Layouts in Blender

## Summary

This pull request introduces two utility functions for automating the process of loading image files from a directory and displaying them as image planes in Blender. The primary goal is to streamline the setup of multiple image screens arranged either in an arc or a grid, with orientation and spacing logic that preserves visual clarity and proportion.

## Functions Included

- `screen_arc_creator(folder_path)`:  
  Arranges image planes in an arc-shaped layout using trigonometric positioning (sine/cosine). The arc curves the images around a central point with consistent spacing. Each image is applied as a material to a plane and rotated to face the arc's center.

- `screen_grid_creator(folder_path)`:  
  Places image planes in a 2D grid layout that automatically adjusts the number of rows and columns to approximate a 16:9 aspect ratio. Planes are uniformly scaled and aligned along the X and Z axes with vertical rotation applied (standing upright). The grid is centered in 3D space.

## Features

- Auto-loads `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`, and `.tga` files from the specified folder.
- Dynamically scales and positions planes.
- Automatically applies image textures as materials.
- Grid layout adapts to image count while maintaining visual balance.
- Clean, center-aligned scene setup for both arc and grid styles.

## Notes

- Planes are given descriptive names matching their image filenames for easier scene management.
- `screen_grid_creator` prefers horizontal expansion (wider than tall) to better simulate screen walls or monitor arrangements.
- Designed for use in Blender 4.4.3 and Python 3.13.4.
