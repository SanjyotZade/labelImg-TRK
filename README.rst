LabelImg-TRK
========

LabelImg-TRK is a graphical image annotation tool.

It is written in Python and uses Qt for its graphical interface.

Tracking has been recently added to LabelImg-TRK to fasten the data annotation process. Consecutive images should have same dimensions.

Annotations are saved as XML files in PASCAL VOC format, the format used
by `ImageNet <http://www.image-net.org/>`__.  Besides, it also supports YOLO format

.. image:: https://raw.githubusercontent.com/tzutalin/labelImg/master/demo/demo3.jpg
     :alt: Demo Image

.. image:: https://raw.githubusercontent.com/tzutalin/labelImg/master/demo/demo.jpg
     :alt: Demo Image

`Watch a demo video <https://youtu.be/p0nR2YsCY_U>`__

Installation
------------


Build from source
~~~~~~~~~~~~~~~~~

Linux/Ubuntu/Mac requires at least `Python
2.6 <https://www.python.org/getit/>`__ and has been tested with `PyQt
4.8 <https://www.riverbankcomputing.com/software/pyqt/intro>`__. However, `Python
3 or above <https://www.python.org/getit/>`__ and  `PyQt5 <https://pypi.org/project/PyQt5/>`__ are strongly recommended.


Ubuntu Linux
^^^^^^^^^^^^
Python 2 + Qt4

.. code:: shell

    sudo apt-get install pyqt4-dev-tools
    sudo pip install lxml
    sudo pip install opencv-python opencv-contrib-python
    make qt4py2
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Python 3 + Qt5 (Recommended)

.. code:: shell

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install -r requirements/requirements-linux-python3.txt
    make qt5py3
    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

macOS
^^^^^
Python 2 + Qt4

.. code:: shell

    brew install qt qt4
    brew install libxml2
    make qt4py2
    pip install opencv-python opencv-contrib-python
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Python 3 + Qt5 (Recommended)

.. code:: shell

    brew install qt  # Install qt-5.x.x by Homebrew
    brew install libxml2

    or using pip

    pip3 install pyqt5 lxml # Install qt and lxml by pip

    make qt5py3
    pip install opencv-python opencv-contrib-python
    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]


Python 3 Virtualenv (Recommended)

Virtualenv can avoid a lot of the QT / Python version issues

.. code:: shell

    brew install python3
    pip3 install pipenv
    pipenv --three # or pipenv install pyqt5 lxml
    pipenv run pip install pyqt5 lxml opencv-python opencv-contrib-python
    pipenv run make qt5py3
    python3 labelImg.py
    [Optional] rm -rf build dist; python setup.py py2app -A;mv "dist/labelImg.app" /Applications

Note: The Last command gives you a nice .app file with a new SVG Icon in your /Applications folder. You can consider using the script: build-tools/build-for-macos.sh


Windows
^^^^^^^

Install `Python <https://www.python.org/downloads/windows/>`__,
`PyQt5 <https://www.riverbankcomputing.com/software/pyqt/download5>`__
and `install lxml <http://lxml.de/installation.html>`__.

Install opencv-python opencv-contrib-python (for windows)

Open cmd and go to the `labelImg <#labelimg>`__ directory

.. code:: shell

    pyrcc4 -o line/resources.py resources.qrc
    For pyqt5, pyrcc5 -o libs/resources.py resources qrc
    
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Windows + Anaconda
^^^^^^^^^^^^^^^^^^

Download and install `Anaconda <https://www.anaconda.com/download/#download>`__ (Python 3+)

Open the Anaconda Prompt and go to the `labelImg <#labelimg>`__ directory

.. code:: shell

    conda install pyqt=5
    conda install opencv-python opencv-contrib-python
    pyrcc5 -o libs/resources.py resources.qrc
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]


You can pull the image which has all of the installed and required dependencies. `Watch a demo video <https://youtu.be/nw1GexJzbCI>`__

Usage
-----

Steps (PascalVOC)
~~~~~~~~~~~~~~~~~

1. Build and launch using the instructions above.
2. Click 'Change default saved annotation folder' in Menu/File
3. Click 'Open Dir'
4. Click 'Create RectBox'
5. Click and release left mouse to select a region to annotate the rect
   box
6. You can use right mouse to drag the rect box to copy or move it

The annotation will be saved to the folder you specify.

You can refer to the below hotkeys to speed up your workflow.

Steps (YOLO)
~~~~~~~~~~~~

1. In ``data/predefined_classes.txt`` define the list of classes that will be used for your training.

2. Build and launch using the instructions above.

3. Right below "Save" button in the toolbar, click "PascalVOC" button to switch to YOLO format.

4. You may use Open/OpenDIR to process single or multiple images. When finished with a single image, click save.

A txt file of YOLO format will be saved in the same folder as your image with same name. A file named "classes.txt" is saved to that folder too. "classes.txt" defines the list of class names that your YOLO label refers to.

Note:

- Your label list shall not change in the middle of processing a list of images. When you save an image, classes.txt will also get updated, while previous annotations will not be updated.

- You shouldn't use "default class" function when saving to YOLO format, it will not be referred.

- When saving as YOLO format, "difficult" flag is discarded.

.. _header-obj-trac:

Object Tracking
~~~~~~~~~~~~~~~

1. Tag an bounding box in any image as describe above. Make sure tracking check-box is tick. Select preferred tracking algorithm.

2. Now when you open the "next image" with keyboard short "d", the same bounding box is tracked automatically for you in the "next image" with the same annotation as previous image.

3. Then you can also add more custom bounding boxes &/or alter tracked bounding boxes.

4. Tracking process can be stopped either by un-ticking tracking check-box, or by deleting all the bounding boxes in the current image.

5. Currently the LabelImg-TRK supports 6-7 different tracking algorithms. Some deep learning based tracking algorithms are coming soon.

Note:

- Tracked bounding boxes for the "next image" will **only be created if the dimensional of two images are same.** ("current image with bounding box" & "next image")

- Tracked bounding boxes for the "next image" will only be created if there are no previously saved bounding boxes for that "next image".

- Tracked bounding boxes will be automatically saved to corresponding xml/txt, unless they are explicitly altered.

- Bounding boxes are only tracked when you move to next image, moving backward (shortcut "a") will not trigger tracking.

- Multiple bounding boxes can be tracked simultaneously.

- If tracker has predicted bounding boxes then log will appear in the title of the "LabelImg-TRK" app, notifying some information.

- While your on the "next image", all the bounding boxes those have been generated by tracking will have reddish highlight when you click on them. (general bounding boxes have blue highlights)

- If you move to image after "next image" (with or without tracking) then reddish highlight will be replaced to conventional blue highlight.

- Finally, when you have finished annotations. And are just cross checking the annotations, make sure to un-tick the tracking check-box.


Create pre-defined classes
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can edit the
`data/predefined\_classes.txt <https://github.com/tzutalin/labelImg/blob/master/data/predefined_classes.txt>`__
to load pre-defined classes

Hotkeys
~~~~~~~

+------------+--------------------------------------------+
| Ctrl + u   | Load all of the images from a directory    |
+------------+--------------------------------------------+
| Ctrl + r   | Change the default annotation target dir   |
+------------+--------------------------------------------+
| Ctrl + s   | Save                                       |
+------------+--------------------------------------------+
| Ctrl + d   | Copy the current label and rect box        |
+------------+--------------------------------------------+
| Space      | Flag the current image as verified         |
+------------+--------------------------------------------+
| w          | Create a rect box                          |
+------------+--------------------------------------------+
| d          | Next image                                 |
+------------+--------------------------------------------+
| a          | Previous image                             |
+------------+--------------------------------------------+
| del        | Delete the selected rect box               |
+------------+--------------------------------------------+
| Ctrl++     | Zoom in                                    |
+------------+--------------------------------------------+
| Ctrl--     | Zoom out                                   |
+------------+--------------------------------------------+
| ↑→↓←       | Keyboard arrows to move selected rect box  |
+------------+--------------------------------------------+

**Verify Image:**

When pressing space, the user can flag the image as verified, a green background will appear.
This is used when creating a dataset automatically, the user can then through all the pictures and flag them instead of annotate them.

**Difficult:**

The difficult field is set to 1 indicates that the object has been annotated as "difficult", for example, an object which is clearly visible but difficult to recognize without substantial use of context.
According to your deep neural network implementation, you can include or exclude difficult objects during training.


Thank you @tzutalin & License
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This annotation tool was originally build by tzutalin. This is just an extension of his work.

`Free software: MIT license <https://github.com/tzutalin/labelImg/blob/master/LICENSE>`_

Citation: Tzutalin. LabelImg. Git code (2015). https://github.com/tzutalin/labelImg


.. image:: https://forthebadge.com/images/badges/built-with-love.svg
        :target: https://github.com/SanjyotZade/labelImg-TRK

Author: `SanjyotZade <http://www.sanjyot.info/>`__
