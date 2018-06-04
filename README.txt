Simple python GUI program to easily use Tensorflow library. Program is written in Python 2.7 and i used PyQt4 for GUI.
Put your train images to separated to categories folders in ./tensorflow-for-poets-2/tf_files
In this presentation of Tensorflow library i retrain MobileNet which  can be configurable in two ways:

	Input image resolution: 128,160,192, or 224px. Unsurprisingly, feeding in a higher resolution image takes more processing time, but results in better classification accuracy.

	The relative size of the model as a fraction of the largest MobileNet: 1.0, 0.75, 0.50, or 0.25.

For this case i used: 224 0.5

	IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

To run program in project folder run:	python -m script.py

To retrain your network put enter number of steps i click "Retrain button" (recommended more than 5000 steps)

To load image File>Load image> and choose your .png file to test

To see results of recognition click "Start" button.


The projects is just small presentation of Tensorflow. The project is being improved all the time



