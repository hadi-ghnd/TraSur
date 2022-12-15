# Traffic-Object-Detection
A Dataset for Object Detection in Traffic Surveillance

### Data link
You can download the dataset [here](https://drive.google.com/file/d/1zYQkN0TPsjJbDJHKmGXJIEzB5EHxqfWE/view?usp=share_link)

### Dataset description
* 23883 images:
  * 16718 train
  * 4777 validation
  * 2388 test

* Five classes:
  * pedestrian
  * cyclist
  * car
  * bus
  * truck
  
* Annotation format:
  * YOLO [darknet](https://github.com/AlexeyAB/darknet#:~:text=com/AlexeyAB/Yolo_mark-,It,-will%20create%20.txt) 

Locating the objects of interest is the most crucial step in the pipeline of traffic video analytics systems as it is the basis for all the consecutive steps. The deep learning algorithms that work based convolutional neural networks require a large amount of training data to perform at an acceptable level. Currently, the most representative object detection method is [YOLOv7](https://github.com/WongKinYiu/yolov7), which surpasses all known object detectors in both speed and accuracy and has 69.7% average precision when tested on the COCO dataset which is the highest accuracy among all known real-time object detectors. However, this performance is not good enough for real-world traffic surveillance systems.

To improve the accuracy of object detection, we have collected a new dataset of traffic surveillance videos and annotated the objects of interest in a number of frames using the [CVAT](https://www.cvat.ai/) tool. After data augmentation, the size of the dataset is increased to 23883 images. These images are split into three groups where 16718 images are used for training, 4777 images are used for validation, and 2388 images are used for testing. After training the YOLOv7 model with the new dataset, we compared the results with the model that was trained on the COCO data and noticed significant improvements. While the average precision of the model trained on COCO data on our dataset is 64.1%, our model achieves 91.3% precision. The dataset has five classes, including pedestrian, cyclist, car, bus, and truck. Pickup trucks and vans are under the car categories and trucks only include the large trucks.

![WeChat Screenshot_20221215094146](https://user-images.githubusercontent.com/24352869/207889539-6760ef1f-68cf-46de-b0db-3f3b4296ff2e.png)



### Data augmentation

Class imbalance is one of the common characteristics of the real-world collected datasets. If the number of instances for one object is more than another across the dataset, it results in class imbalance. The prediction results can be biased against the underrepresented objects and in favor of the categories with more abundant instances. For example, in a typical urban traffic environmnet, there are more instances of cars than buses and cyclists. Hence, the car category in the collected dataset tends to dominate the majority of the objects. This results in the trained model misclassifying the objects of the minority categories, such as bus and truck.
In order to improve vehicle type classification accuracy, we have trained a new model to classify vehicles into cars, buses, and trucks, respectively. Note that a lot of trucks and buses can not be correctly classified using the current popular deep learning models. This is mainly due to the unbalanced training data.Figure shows that the number of cars in the training dataset is always over ten times the number of the trucks and buses in regular datasets. Such an unbalanced training data set often leads to incorrect classification results, namely, trucks and buses are often not classified correctly.

![Untitled](https://user-images.githubusercontent.com/24352869/207986413-65e3bedf-4eb7-4c2d-a47a-a66fb7e817c1.png)


Several techniques have been used to augment the dataset by creating new images and increasing the number of samples from underrepresented classes. These techniques include Gaussian blur, fancy PCA, histogram equalization, Gaussian noise, image inversion, image normalization, pixel dropout, sharpening, solarization, and random changes in color, brightness, hue, saturation, and contrast values. The [albumentation repository](https://github.com/albumentations-team/albumentations) is used. We have created synthetic images by cropping out objects form the original images and placing them on the subtracted background of the videos, which does not contain any objects from the target classes. Specifically, we first applied the MOG method to subtract the background of the videos. This method employs the motion information to subtract the stationary background from the moving objects, e.g. vehicles. Then object instances of minority categories are placed on the subtracted background to create a new synthetic image. These images is further augmented with several transformations.


![WeChat Screenshot_20221215094515](https://user-images.githubusercontent.com/24352869/207890370-a83430d8-2da3-43be-98b1-7597e9f72835.png)


### Citation
```
@misc{Ghahremannezhad_TraSur_Dataset_for_2022,
  author = {Ghahremannezhad, Hadi},
  title = {{TraSur Dataset for Object Detection in Traffic Surveillance Videos}},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/hadi-ghnd/TraSur}},
  version = {1.0.0},
  year = {2022}
}
```
