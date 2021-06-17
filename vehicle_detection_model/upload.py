from firebase_admin import credentials, initialize_app, storage
cred = credentials.Certificate(r'C:\simple-faster-rcnn-pytorch-master\fypdb-ivanleinnn-firebase-adminsdk-k3fih-f47cdfef00.json')
initialize_app(cred, {'storageBucket': 'fypdb-ivanleinnn.appspot.com'})

filePath = r'C:\Web_scrapper\mcdowell_rd.jpg'
bucket = storage.bucket()
blob = bucket.blob('mcdowell_rd')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\mcdowell_rd_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('mcdowell_rd_detected')
blob.upload_from_filename(filePath)

filePath = r'C:\Web_scrapper\90th_st.jpg'
bucket = storage.bucket()
blob = bucket.blob('90th_st')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\90th_st_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('90th_st_detected')
blob.upload_from_filename(filePath)

filePath = r'C:\Web_scrapper\camelback_rd.jpg'
bucket = storage.bucket()
blob = bucket.blob('camelback_rd')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\camelback_rd_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('camelback_rd_detected')
blob.upload_from_filename(filePath)

filePath = r'C:\Web_scrapper\glendale_ave.jpg'
bucket = storage.bucket()
blob = bucket.blob('glendale_ave')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\glendale_ave_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('glendale_ave_detected')
blob.upload_from_filename(filePath)

filePath = r'C:\Web_scrapper\northern_ave.jpg'
bucket = storage.bucket()
blob = bucket.blob('northern_ave')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\northern_ave_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('northern_ave_detected')
blob.upload_from_filename(filePath)

filePath = r'C:\Web_scrapper\via_de_ventura.jpg'
bucket = storage.bucket()
blob = bucket.blob('via_de_ventura')
blob.upload_from_filename(filePath)
filePath = r'C:\simple-faster-rcnn-pytorch-master\imgs\via_de_ventura_detected.jpg'
bucket = storage.bucket()
blob = bucket.blob('via_de_ventura_detected')
blob.upload_from_filename(filePath)