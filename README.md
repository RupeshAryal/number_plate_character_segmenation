## number_plate_character_segmenation

## To run the algorithm in browser, use the following step:

- Clone the Repository into your local machine.
- Create a python Virtual Environment environment.
- Install the packages from requirements.txt file
- On your terminal type "streamlit run app.py"
- upload the image to the uploaded and see the result. You can use sample datasets included in this repo. 


## Current Progress of the Project

- *Trained devanagari character dataset for different nepali characters. The training model is saved in file Model.h5**
- **Image Processsing**
  -  For Character Segmentation, contour based image segmentation method is used.
  -  Used histogram equilization (CLAHE) to increase the image contrast.
  -  For noise removal, I applied Gaussian Blur which was then followed by dilation and erosion.

- **Contour Filtering and Prediction**
  - Despite preprocessing, the algorithm was unable to remove all the noises. Which I assumed was due to the variation of conditions in which the images were taken. Some of the plates had excessive dirts, some if them had characters faded and some of them were over exposed or underexposed. 
 
  - Since the noise present in the images were not completeley removed, the contours were also created for such small noises as well. However, the contours from the noise had some distinct characteristics. For eg: dirt or any small particles were very small in size and their respective contour were also identitcal. I filtered out such noises by discarding the contour which had size less than (15x15) pixel. 
 
  - Characters in the number plate has a unique characteristic in the dataset. That is, they are uniform across height and width. Meaning, if a contour for a character is drawn. The width and height of such counter do not differ by a big value. Contours with very high width but very small height and vice versa were discarded and were considered as being a outlier. I have used a threshold of 0.6(60%) to filter these contours i.e contours have more than 60% difference between width and height were discarded.
 
  - After the contours have been filtered out, bounding boxes were drawn around those contour, the region was then cropped out and the cropped section of image was given as an output to the model inorder to recognize the character. 
 
- **Limitations and Problems**
  - This algorithm works well for plates which is in good condition and has well seperated characters. But for plates with some distortion it is unable to segment the regions containing text.
  - Number plates having small size, but many characters (eg: Number plates from bike) were not segmented properly.
  - While, the algorithm works and the order of character is correct in case of single row number plate. The characters are not ordered in a way a normal person reads a number plate. However, I am exploring possible use of histogram based line segmentation , which uses distribution of intensities to seperate the lines.

##Future Direction

In the next version of the project I will be using CNN based architecture for character segmentation and detection.


## Some example from this version of the project

## Working Examples

![working_example](/progress_image/working1.png) ![working_example](/progress_image/working2.png) ![working_example](/progress_image/working3.png) ![working_example](/progress_image/working4.png) ![working_example](/progress_image/working5.png) ![working_example](/progress_image/working6.png) ![working_example](/progress_image/working7.png) ![working_example](/progress_image/working8.png) ![working_example](/progress_image/working9.png) ![working_example](/progress_image/working10.png) ![working_example](/progress_image/working11.png) ![working_example](/progress_image/working12.png) ![working_example](/progress_image/working13.png) ![working_example](/progress_image/working14.png) ![working_example](/progress_image/working15.png) ![working_example](/progress_image/working16.png) ![working_example](/progress_image/working17.png) ![working_example](/progress_image/working18.png)  ![working_example](/progress_image/working1.png) 

## Examples that segments characters but includes noise as well

![working_example](/progress_image/noise_included1.png) ![working_example](/progress_image/noise_included2.png) ![working_example](/progress_image/noise_included3.png) ![working_example](/progress_image/noise_included4.png)
![working_example](/progress_image/noise_included5.png) ![working_example](/progress_image/noise_included6.png) ![working_example](/progress_image/noise_included7.png) ![working_example](/progress_image/noise_included8.png)
![working_example](/progress_image/noise_included9.png) ![working_example](/progress_image/noise_included10.png) ![working_example](/progress_image/noise_included11.png) ![working_example](/progress_image/noise_included12.png)

## Not Working

![working_example](/progress_image/not_working1.png) ![working_example](/progress_image/not_working2.png) ![working_example](/progress_image/not_working3.png) ![working_example](/progress_image/not_working4.png) ![working_example](/progress_image/not_working5.png) ![working_example](/progress_image/not_working6.png) ![working_example](/progress_image/not_working7.png) ![working_example](/progress_image/not_working8.png) ![working_example](/progress_image/not_working9.png) ![working_example](/progress_image/not_working10.png) ![working_example](/progress_image/not_working11.png) ![working_example](/progress_image/not_working12.png) ![working_example](/progress_image/not_working13.png) ![working_example](/progress_image/not_working14.png) ![working_example](/progress_image/not_working15.png) ![working_example](/progress_image/not_working16.png)

 

 
	
 
