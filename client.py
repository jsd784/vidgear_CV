# import required libraries
from vidgear.gears import NetGear
import cv2
from gluoncv import model_zoo, data, utils
import mxnet as mx

# np.set_printoptions(threshold=sys.maxsize)

# define Netgear Client with `receive_mode = True` and default parameter
client = NetGear(logging=True,receive_mode=True)

#Initialize the model
net = model_zoo.get_model('ssd_512_mobilenet1.0_voc_int8', pretrained=True,root="ssd_512_mobilenet1_int8")

# Compile the model for faster speed
net.hybridize(static_alloc=True,static_shape=True)

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # Image pre-processing
    frame = mx.nd.array(frame,dtype="uint8")
    rgb_nd, scaled_frame = data.transforms.presets.ssd.transform_test(frame, short=512)
    
    # cv2.imshow("Output Frame", frame.asnumpy())
    
    # Run frame through network/model
    class_IDs, scores, bounding_boxes = net(rgb_nd)
    
    # Post Processing
    scale = 1.0 * frame.shape[0] / scaled_frame.shape[0]
    img = utils.viz.cv_plot_bbox(frame.asnumpy(), bounding_boxes[0], scores[0], class_IDs[0], class_names=net.classes, scale=scale)

    # Display the result
    cv2.imshow("Output Frame", img)
        
    # check for received frame if Nonetype
    if frame is None:
        break
    
    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()
