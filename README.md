# PitDensityImageProcessingCalculator
This repository is for calculating pit density from an image. This converts images to r,g,b or r+g+b co-ordinates, then binarizes the image based on a user-input threshold level, then can invert the binarized image color, and finally detects the number of pits. A second function finds the size of the image. Finally the pit density is calculated.

The code is sensitive to differences in light levels throughout the image, so ideally lighting is consistent and even throughout the image. This code also works best when the appropriate color is chosen. For example, a red rust spot on a metal background would show the highest contrast in a 'r' color, and dark colored pits on a lighter surface would show the highest contrast in 'r+g+b' color.

This code is subjective and requires users to play around with the settings, but simplifies images that have many pits in them.
