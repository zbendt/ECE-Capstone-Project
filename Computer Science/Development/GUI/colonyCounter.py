import cv2
import numpy as np;
font = cv2.FONT_HERSHEY_SIMPLEX
text_loc = (20, 40)
font_scale = 1
font_color = (255,0,0)
line_type = 2

def analyzeImage(imageNumber):
    #setup
    colonyCount = 0  # initalizes  
    fileName = "/home/pi/Documents/deltaImageProcessor/images/"\
             + str(imageNumber) + ".jpg"
    
    #import sample image
    image = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)  

    #Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 100

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1
    params.maxArea = 1000

     # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0
    params.maxCircularity = 1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.1

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.05

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
     
    # Detect colonies.
    identifiers = detector.detect(image)
    colonyCount = len(identifiers)
    
    # place red circles around blobs.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_identifiers = cv2.drawKeypoints(image, identifiers, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_count = cv2.putText(im_with_identifiers, str(colonyCount), text_loc, font, font_scale, font_color, line_type)
    
    # Show display image with keypoints and count
    #cv2.imshow("Sample " + str(imageNumber), im_with_count)
    cv2.imwrite("/home/pi/Documents/deltaImageProcessor/images_with_keys/" + str(imageNumber) + ".jpg", im_with_count)
    #cv2.waitKey(500)
    
    return colonyCount
