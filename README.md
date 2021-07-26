# Abusive Text or Hatespeech Detection API

## Dataset Used
- A Mixture of Multiple Datasets that mark the presence of hatespeech or abusive language. Along with a list of randomly generated text that's devoid of any. The Data is Custom Made.
- I've used different classifiers and the scores produced are a mixture of multiple results.

## Architecture and Models
- Classification using simple Naive Bayes
- Support Vector Machines
- Word Embeddings with Gensim and Keras Classification
- The Final Result is a mixture of scores from the above Models.

## The output
- The API Page
<img src="https://github.com/reekithak/Abusive-Text-Hatespeech-Detection/blob/main/images/1..JPG">

- Test 1
<img src="https://github.com/reekithak/Abusive-Text-Hatespeech-Detection/blob/main/images/2..JPG">

- Test 2
<img src="https://github.com/reekithak/Abusive-Text-Hatespeech-Detection/blob/main/images/3..JPG">


## Run the Application in your Device? 
- Once all the Above is Completed , Lets run our Application. There are Certain parameters to consider.

'--weights'     => 'model.pt path(s)'<br />
'--source'      =>'# file/folder, 0 for webcam<br />
'--img'         =>'inference size (pixels)'<br />
'--conf'        =>'object confidence threshold'<br />
'--iou'         =>'IOU threshold for NMS'<br />
'--device'      =>'cuda device, i.e. 0 or 0,1,2,3 or cpu'<br />
'--view-img'    =>'display results'<br />
'--save-txt'    =>'save results to *.txt'<br />
'--save-conf'   =>'save confidences in --save-txt labels'<br />
'--save-crop'   =>'save cropped prediction boxes'<br />
'--nosave',     =>'do not save images/videos'<br />
'--classes'     =>'filter by class: --class 0, or --class 0 2 3'<br />
'--agnostic-nms'=>'class-agnostic NMS'<br />
'--augment'     =>'augmented inference'<br />
'--update'      =>'update all models'<br />
'--project'     =>'save results to project/name'<br />
'--name'        =>'save results to project/name')<br />
'--exist-ok'    =>'existing project/name ok, do not increment'<br />

- To Generally run the Application with a confidence of 30% via WebCam use this command from the root of the Repository<br />
`python detect.py --weights best.pt --img 412 --conf 0.3 --source 0`


## Note: 
- Open Source Code Used
