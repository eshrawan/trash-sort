#!/usr/bin/env python

# import required libs and functions
from classify_image import run_inference_on_image
from class_list import class_dictionary
import picamera
import gc

# Set trash type hash
waste_type = {"r":"Recycling", "c":"Compost"}

class_dictionary = class_dictionary();


def predict_top_5(image_url):
    print("Tensorflow is processing the image...")
    return run_inference_on_image(image_url)


def top_prediction_name(prediction):
    return prediction[4]


def what_is_it(image_name):
    image_path = image_name
    print("2")  # Setting variable for image filepath.
    top_5 = predict_top_5(image_path)  # Pulling-out the top 5 matched results
    print (top_5)

    top = top_5[4]
    print("3")  # Pulling-out the top class
    top_name = top[0]  # Pulling-out the top class name

    print ("THE OBJECT WAS: " + top_name)

    if class_dictionary[top_name] == 'c':
        return 'c'
    else: 
        return 'r'


def ClickPicture():
	filename="photo.jpg"
	try:
		camera = picamera.PiCamera()
		camera.resolution = (256,192)
		camera.brightness = 70
		camera.contrast = 70
		camera.saturation = 0
		camera.awb_mode = 'incandescent'
		camera.capture(filename)
		print("Photo Saved: "+filename)
	finally:
		camera.close()
	return filename

def MasterFunction():
        image_name = ClickPicture()
        print("1")
        trash_type = what_is_it(image_name)
        print ("WASTE TYPE: " + waste_type[trash_type])

        if trash_type == "r":
            print ("r")
        else:
            print ("c")
            
        del image_name

while (1):
	MasterFunction()
	gc.collect()


# # webapp
# from flask import Flask, jsonify, render_template, request

# app = Flask(__name__)

# @app.route('/display', methods=['POST'])
# def display():
#     obj_name = top_name
#     obj_type = class_dictionary[top_name]
#     return jsonify(results=[obj_name, obj_type])

# @app.route('/')
# def main():
#     return render_template('index.html')
