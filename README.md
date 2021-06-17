Attention!!!
This repo does not contain any gradle, dependencies and node modules files due to size limitation, you need to modify the gradle and install dependency by yourself (include firebase, react-native-maps,react-native-svg and react-native)

'/vehicle_detection_model' is the faster-rcnn object detection model of the system

'/trafficmonitoringsystem' is the mobile application of the system

'/Web_scraper' is the web scraper of the system

you need to edit the file path used in the python file in order to run it correctly, for example change the file path of run.py in line 26 from r'C:\vehicle_detection_model\model\fasterrcnn_55235744.pth' to r'your_local_machine_file_path' to load the vehicle detection model correctly

Step of running this system:
1. execute run.bat in 'vehicle_detection_model' to run the web scraper and vehicle detection model periodically
	1.1 in order to exectue run.bat correctly you to to install python library by the following command "pip install pytorch torchvision cudatoolkit=10.2 -c pytorch" and "pip install visdom scikit-image tqdm fire ipdb pprint matplotlib torchnet"
2. execute  command "npx react-native run-android "to run App.js which is the mobile application (you need to install android emulator or connected to a real android device)

Detected Image:
![img](vehicle_detection_model/imgs/90th_st_detected.jpg)
![img](vehicle_detection_model/imgs/camelback_rd_detected.jpg)
![img](vehicle_detection_model/imgs/glendale_ave_detected.jpg)
![img](vehicle_detection_model/imgs/mcdowell_rd_detected.jpg)
![img](vehicle_detection_model/imgs/northern_ave_detected.jpg)
![img](vehicle_detection_model/imgs/via_de_ventura_detected.jpg)
