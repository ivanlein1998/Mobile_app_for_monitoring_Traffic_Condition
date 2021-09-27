## 1. Introduction
The Traffic Monitoring Systemt is a mobile application of traffic monitoring system that using Faster-RCNN object detection model to count the total number of vehicles in specific road or highway and show the information on mobile app, so that driver can have better understanding of traffic condition on different traffic hotspots. 

It require live webcast image of main road for model training and traffic condition monitoring. On Arizona Department of Transport, they provide a http path for user to get image from their server, we can use https://www.az511.gov/map/Cctv/XXXX-XX (XXXX-Xx represent the webcast ID) to get access with the target road snapshot, all of the data will be stored in Firebase Realtime Database so that user can retrieve the data once the traffic condition is updated and display the information on mobile application interface

## 2. Installation
you need to edit the file path used in the python file in order to run it correctly, for example change the file path of run.py in line 26 from r'C:\vehicle_detection_model\model\fasterrcnn_55235744.pth' to r'your_local_machine_file_path' to load the vehicle detection model correctly

Step of running this system:
1. execute run.bat in 'vehicle_detection_model' to run the web scraper and vehicle detection model periodically
	1.1 in order to exectue run.bat correctly you to to install python library by the following command "pip install pytorch torchvision cudatoolkit=10.2 -c pytorch" and "pip install visdom scikit-image tqdm fire ipdb pprint matplotlib torchnet"
2. execute  command "npx react-native run-android "to run App.js which is the mobile application (you need to install android emulator or connected to a real android device)

## 3. Object detection model structure:
Torchvision framework has been used for backbone build the Faster-RCNN object detection model, I use torchvision pretrained VGG16 model as my object detection backbone, VGG 16 contain 16 layers ( 13 convolutional layers and 3 fully-connected layers.
The VGG16 Faster-RCNN object detection model in this project include 6 components, 5 convolutional block  and one fully-connected classifier. The filter size of the 1st ,2nd ,3rd ,4th and  5th convolutional block are 64, 128, 256, 512 and 512 respectively, they are used for max pooling that will take the largest element of the previous feature generated by convolutional layer and refined feature map. The last component is fully-connected classifier, the flatten layer will flatten the data from previous convolutional block into 1D format (I set the size to 4096 in this project) and use dense layer to input the data into the Faster-RCNN object detection model.

![img](imgs/FYP_model_structure.png)


## 4. Smaeple Detected Image:
![img](vehicle_detection_model/imgs/90th_st_detected.jpg)
![img](vehicle_detection_model/imgs/camelback_rd_detected.jpg)
![img](vehicle_detection_model/imgs/glendale_ave_detected.jpg)
![img](vehicle_detection_model/imgs/mcdowell_rd_detected.jpg)
![img](vehicle_detection_model/imgs/northern_ave_detected.jpg)
![img](vehicle_detection_model/imgs/via_de_ventura_detected.jpg)

## 5.  Training result 
The training result of the Faster-RCNN model is visualized by visdom, here are one of the training data visualizztion photo:
![img](imgs/4_cap.png)
The final performance of object detection is:
|              mAP              |     0.69     |
|               total loss              |     0.23     |
|               classification loss              |     0.023     |
|              bounding box regression loss              |     0.036     |

## 6.  Mobile Application interface:
The Mobile application is developed on React Native and connected to Google Maps API (React_Native_Maps), Google Maps allow developer to customized the maps, mobile application will retrieve the traffic data from database, and then use data – VehiceleCount to create a marker, the icon of the marker represent the number of car detected in that road.

![img](imgs/image.jpg)

## 7.  Attention!!!
This repo does not contain any gradle, dependencies and node modules files due to size limitation, you need to modify the gradle and install dependency by yourself (include firebase, react-native-maps,react-native-svg and react-native)

'/vehicle_detection_model' is the faster-rcnn object detection model of the system
'/trafficmonitoringsystem' is the mobile application of the system
'/Web_scraper' is the web scraper of the system
