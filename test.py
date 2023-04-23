from roboflow import Roboflow
rf = Roboflow(api_key="sRuK1fNu4nEl0kkAGNDl")
project = rf.workspace().project("hackathon-edexl")
model = project.version(1).model

# infer on a local image
predictions = model.predict("b4.png", confidence=40, overlap=30).json()


import cv2

# Load the image
image = cv2.imread(predictions['predictions'][0]['image_path'])

# Get the coordinates and size of the bounding box
x = predictions['predictions'][0]['x']
y = predictions['predictions'][0]['y']
w = predictions['predictions'][0]['width']
h = predictions['predictions'][0]['height']

# Draw the bounding box on the image
cv2.rectangle(image, (x, y), ( x-w, 1 ), (0, 255, 0), 2)

# Save the image with the bounding box
cv2.imwrite("output.jpg", image)
