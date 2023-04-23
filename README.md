# DAPR
A web-based tool that utilizes machine learning algorithms to analyze health insurance claims data and detect potential fraud


##Health Insurance Fraud Detection Model

This repository contains a machine learning model that can be used to detect fraudulent health care insurance claims and a custom object detection model. 
The first model was trained on a dataset of health care insurance claims that were labeled as either fraudulent or legitimate. The model was built using Python and scikit-learn.
The working of this model is primarly based on Logistic Regression as it is a typical case of binary classification.

For the second model, we have created a custom object detection model using YOLO8, RoboFlow and few python libraries.
Rather than deploying the model on a website we have shown the object detection results produced by the model in  test.ipnyb file itself.
Also there are few attached screenshots of models's accuracy on roboflow with its  yolo code in ipnyb format file.


## Installation

To use fraud detection model, you will need to have PyCharm or Anaconda/Jupyter notebook installed on your computer. 
create an epmty folder on desktop and open terminal in it, type jupyter notebook command to launch jupyter notebook or directly open pycharm and select the folder you want, if working on pycharm
install numpy,matplotlib,pandas and scikit learn using pip install lib_name in the terminal or cmd prompt


##Deployement

The model was deployed at the backend of the website using “python Flask”. The IDE used for this purpose was pycharm.
It was required to upload the csv files and its converted pickle file. The pickle file was converted in the jupyter notebook itself. 
It was also required to upload the frontend part on pycharm (templates folder which is its default folder)
Static folder was uploaded for uploading the images and css file.


## Usage

Once you have installed the required packages, you can use the model to detect fraudulent health care insurance claims by running the following command in your terminal:
Also the second model can be used for object detection purposes.

NOTE:
In order to check for fraud, there are 19 input fields that need to be filled by the user. All the fields listed in the form MUST be filled. 
After you have entered this information, the model will use it to make a prediction about whether the health care insurance claim is fraudulent or legitimate.

Model-1  Accuracy: 63%
Model-2  Accuracy: 99%


## Contributing

	Prisha Baveja- github: Prisha-baveja
			Deployment and building of ML model
	Riddhi Maheshwari- github: Riddhi-283
			Deployment and building of ML model
	Diya Anem- github: diyaanem
			Designing webpage- frontend+linking pages
	Anushka Samadder- github: AnushkaSamadder
			Designing webpage- frontend+linking pages

If you find any issues with the model or have suggestions for how to improve it, please feel free to open an issue or submit a pull request.
