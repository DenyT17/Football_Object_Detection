# Football_Object_Detection

## Technologies 💡
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)


## Description ❔❓

In this project in first part I will try to detecting and tracking football players on video. 
When result will be satisfying I will try to map players position on the pitch in to 2D pitch image, thanks to whitch I will be able to analyse strategy of both teams
and players movement in each actions.


## Dataset and auxiliary materials 📁

When creating this project, in few case I used the solution presented at the following link:

[Football players tracking with YOLOv5 + ByteTrack](https://github.com/roboflow/notebooks/blob/main/notebooks/how-to-track-football-players.ipynb?ref=blog.roboflow.com)

Dataset whitch I used to train YOLOv8 model:

[DFL - Bundesliga Data Shootout](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data)

## Model training 

In this part I use YOLOv8 and ByteTrack to detecting and tracing players. 

Training results you can find here : 

[Football_Objects_Detections_Training_model](https://github.com/DenyT17/Football_Object_Detection/blob/main/Football_Objects_Detections_Training_model.ipynb)

** This model will be changed ** 

Thanks to this model I can detected players on the pitch : 

![image](https://user-images.githubusercontent.com/122997699/229868941-d5b1005b-6cca-406a-872c-b4524a144d25.png)


In next step I tracked each player on pitch. 
![image](https://user-images.githubusercontent.com/122997699/229868702-4f7198f5-9355-4717-9ecf-8a6df390d40d.png)

But I decided to create new model, thanks to which I will detecting player in both team.
If result will not be satisfying, I will try to use K-means to detecting jersey colors.


## Next goals 🏆⌛

* Train new model based on image with class like: 
- Team 1
- Team 2
- Referees
- Ball
- Goalkeeper

*  Mapping player position to 2D pitch image

