echo off

:Again  
echo start_web_scrapper
cd C:\Web_scrapper
python C:\Web_scraper\web_scraper.py
echo start_object_detection
cd C:\simple-faster-rcnn-pytorch-master
python C:\vehicle_detection_model\run.py
echo upload_image_and_data_to_database
python C:\vehicle_detection_model\upload.py

goto Again