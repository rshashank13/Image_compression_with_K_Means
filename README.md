# Image_compression_with_K_Means

Here, we take an image of size (120x120x3) and find out 16 major colours (RGB values) using K-means (K=16).
In the original image, each pixel uses 24 bits. By finding 16 major colours we can use just 4 bits for each pixel, where 4 bits can index 16 colours (RGB values).
There by we reduce the size, by using a total space of (16x24)+(120x120x4) bits instead of (120x120x24) bits.
