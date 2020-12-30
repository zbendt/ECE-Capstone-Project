import cv2
import numpy as np;

def analyzeImage(imageNumber):
    #setup
    colonyCount = 0
#     fileName = "/home/pi/Documents/deltaImageProcessor/images/"\
#             + str(imageNumber) + ".jpg"

    fileName = "/home/pi/Documents/BlobTest.jpg"
    image = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)  #import jpeg

    #Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1500

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    params.maxCircularity = .785

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.05

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
     
    # Detect blobs.
    keypoints = detector.detect(image)
    colonyCount = len(keypoints)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
     
    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)
    return colonyCount