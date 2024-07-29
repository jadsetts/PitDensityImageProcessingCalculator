# PitDensityImageProcessingCalculator

![Picture2](https://github.com/user-attachments/assets/f2053edf-edbe-4dec-8423-aeeea205b15a)![Capture](https://github.com/user-attachments/assets/4319df5c-ecba-4e02-8cdb-f7939a435aa5)


This repository is for calculating pit density (pits/mm2) from an image starting with the function 'pitsInImage'. This code is subjective and requires users to play around with the settings, but simplifies images that have many pits in them. This converts images to r, g, b or r+g+b co-ordinates, then binarizes the image based on a user-input threshold level, then can invert the binarized image color, and finally detects the number of pits. A second function (called 'calibrationDistance') finds the size of the image. Finally the pit density is calculated from the number of pits and the area.

The code is sensitive to differences in light levels throughout the image, so ideally lighting is consistent and even throughout the image. This code also works best when the appropriate color is chosen. For example, a red rust spot on a metal background would show the highest contrast in an 'r' color mode, and dark colored pits on a lighter surface would show the highest contrast in a 'binary' color mode.
