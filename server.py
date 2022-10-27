# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear

# open any valid video stream(for e.g `test.mp4` file)
stream = VideoGear(source="streetvideo.mp4").start()
# stream = VideoGear(source="timelapse.mp4").start()
# stream = VideoGear(source="airport.mp4").start()
# stream = VideoGear(source="videos/Free_Test_Data_5MB_AVI.avi", colorspace="COLOR_BGR2GRAY").start()

# activate jpeg encoding and specify other related parameters
# options = {
#     "jpeg_compression": True,
#     "jpeg_compression_quality": 90,
#     "jpeg_compression_fastdct": True,
#     "jpeg_compression_fastupsample": True,
# }


# Define Netgear Server with default parameters
# server = NetGear()
server = NetGear(logging=True)


# for frame in x_test:
#     # print(frame)
    
#     cv2.imshow("Input Frame", frame)
    
#     try:
#         server.send(np.array([frame]))
        
#     except KeyboardInterrupt:
#         break
    

# loop over until KeyBoard Interrupted
while True:

    try:

        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break

        # {do something with the frame here}

        # send frame to server
        server.send(frame)

    except KeyboardInterrupt:
        break

# safely close video stream
stream.stop()

# safely close server
server.close()
