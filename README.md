# study_yolo11

- 图像分类 Image Classification
![](https://github.com/ultralytics/docs/releases/download/0/image-classification-examples.avif)
图像分类是三种任务中最简单的一种，它涉及将整个图像分类到一组预先定义的类别中的一个。图像分类器的输出是一个单一的类别标签和一个置信度分数。当你只需要知道一张图像属于哪个类别，而不需要知道该类别的对象在哪里或者它们的确切形状是什么的时候，图像分类是很有用的。

![](https://github.com/jaybee520/study_yolo11/blob/main/runs/classify/predict/image0.jpg)


 - 实例分割 Instance Segmentation
![](https://github.com/ultralytics/docs/releases/download/0/instance-segmentation-examples.avif)
实例分割比目标检测更进一步，它包括在图像中识别单个对象，并将它们从图像的其余部分分割出来。
实例分割模型的输出是一组掩码或轮廓，它们勾勒出图像中每个对象的轮廓，同时还有每个对象的类别标签和置信度分数。当你不仅需要知道图像中的对象在哪里，还需要知道它们的确切形状时，实例分割非常有用。

![](https://github.com/jaybee520/study_yolo11/blob/main/runs/segment/predict/image0.jpg)


 - 目标检测 Object Detection
![](https://github.com/ultralytics/docs/releases/download/0/object-detection-examples.avif)
物体检测是一项涉及在图像或视频流中识别物体的位置和类别任务。物体检测器的输出是一组包围图像中物体的边界框，以及每个框的类别标签和置信度分数。当你需要在场景中识别感兴趣的物体，但不需要确切知道物体的位置或其确切形状时，物体检测是一个很好的选择。

![](https://github.com/jaybee520/study_yolo11/blob/main/runs/detect/predict/image0.jpg)



 - 姿态预测 Pose Estimation
![](https://github.com/ultralytics/docs/releases/download/0/pose-estimation-examples.avif)
姿态估计是一项涉及识别图像中特定点位置的任务，这些特定点通常被称为关键点。关键点可以代表物体的各个部分，例如关节、地标或其他独特特征。关键点的位置通常表示为一组二维 [x, y] 或三维 [x, y, visible] 坐标。
姿态估计模型的输出是一组代表图像中物体上关键点的点，通常还包括每个点的置信度分数。当你需要识别场景中物体的特定部分以及它们之间的相对位置时，姿态估计是一个很好的选择。

![](https://github.com/jaybee520/study_yolo11/blob/main/runs/pose/predict/image0.jpg)



 - 定向目标检测 Oriented Bounding Boxes Object Detection
![](https://github.com/ultralytics/docs/releases/download/0/ships-detection-using-obb.avif)
![](https://github.com/ultralytics/docs/releases/download/0/vehicle-detection-using-obb.avif)
定向目标检测比目标检测更进一步，引入了一个额外的角度来更准确地定位图像中的物体。定向目标检测器的输出是一组旋转的边界框，这些边界框恰好包围图像中的物体，同时还包括每个框的类别标签和置信度分数。当你需要在场景中识别感兴趣的物体，但不需要确切知道物体在哪里或其确切形状时，目标检测是一个不错的选择。

![](https://github.com/jaybee520/study_yolo11/blob/main/runs/obb/predict/image0.jpg)