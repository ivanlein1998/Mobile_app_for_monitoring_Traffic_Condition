from firebase import firebase
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from utils.config import opt
from model import FasterRCNNVGG16
from trainer import FasterRCNNTrainer
from data.util import  read_image
from utils.vis_tool import vis_bbox
from utils import array_tool as at
import os
import torch as t
import firebase_admin

faster_rcnn = FasterRCNNVGG16()
trainer = FasterRCNNTrainer(faster_rcnn).cuda()

# Use a service account
cred = credentials.Certificate(r'C:\vehicle_detection_model\fypdb-ivanleinnn-firebase-adminsdk-k3fih-f47cdfef00.json')
key= "U4N26iL2IxopTWPQCcF8brgcPjwtpPuQOCzf2Nf3"
authentication = firebase.FirebaseAuthentication(key, 'lein19980131@gmail.com')
firebase.authentication = authentication
user = authentication.get_user()
firebase = firebase.FirebaseApplication('https://fypdb-ivanleinnn-default-rtdb.firebaseio.com/', authentication = authentication)

trainer.load(r'C:\vehicle_detection_model\model\fasterrcnn_55235744.pth')
img = read_image(r'C:\Web_scrapper\northern_ave.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","northern_ave_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\northern_ave_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\northern_ave_detected.jpg')

img = read_image(r'C:\Web_scrapper\glendale_ave.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","glendale_ave_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\glendale_ave_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\glendale_ave_detected.jpg')

img = read_image(r'C:\Web_scrapper\camelback_rd.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","camelback_rd_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\camelback_rd_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\camelback_rd_detected.jpg')

img = read_image(r'C:\Web_scrapper\90th_st.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","90th_st_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\90th_st_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\90th_st_detected.jpg')

img = read_image(r'C:\Web_scrapper\via_de_ventura.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","via_de_ventura_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\via_de_ventura_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\via_de_ventura_detected.jpg')

img = read_image(r'C:\Web_scrapper\mcdowell_rd.jpg')
img = t.from_numpy(img)[None]
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(img,visualize=True)
number_of_bbox = len(at.tonumpy(_bboxes[0]))
firebase.put("/fyp_data","mcdowell_rd_num_of_car", number_of_bbox)
dp = vis_bbox(at.tonumpy(img[0]),
         at.tonumpy(_bboxes[0]),
         at.tonumpy(_labels[0]).reshape(-1),
         at.tonumpy(_scores[0]).reshape(-1))
dp2 = dp.get_figure()
dp2.savefig(r'C:\vehicle_detection_model\imgs\mcdowell_rd_detected.jpg')
dp2.savefig(r'C:\Users\85266\AndroidStudioProjects\trafficmonitoringsystem\imgs\mcdowell_rd_detected.jpg')

