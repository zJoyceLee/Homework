Computer Vision
============

Course lab via Python, OpenCV.

Lab01: flip 1.jpg
----

    python flip.py
    python rotate_image_by_180_degree.py

Lab02: Image Matting, move a tree.
----
* version1
-
Rectangle move.

    python move_tree_roughly.py


* version2
-
counter(255) in n*n matrix > min

    python move_tree_by matrix.py


* version3
-
final version
cv2.COLOR_BGR2GRAY
cv2.findContours()
cv2.drawContours()
cv2.floodFill()

    python move_tree_by_floodfill.py

Lab03: jigsaw, reappear the elephant in 2.jpg.
----

    python tmp.py
