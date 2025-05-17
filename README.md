# 🧠 Vidgear CV Demo

This project demonstrates real-time video streaming and object detection using the [VidGear](https://github.com/abhiTronix/vidgear) networking library and a pre-trained SSD model from [GluonCV](https://cv.gluon.ai/).

The setup includes:
- A **NetGear server** that streams video frames from a local file using `VideoGear`.
- A **NetGear client** that receives frames, performs object detection using `ssd_512_mobilenet1.0_voc_int8`, and visualizes the results.

---

## 📦 Features

- 🔁 **Real-time streaming** of video frames over the network
- 🤖 **Efficient object detection** with GluonCV’s quantized SSD model
- 💡 **Modular design** using Vidgear's `NetGear` and `VideoGear` APIs
- ⚡ Optimized inference using `mxnet` with hybridized models

---

## 📁 Folder Structure

```bash
.
├── server.py   # Streams video frames using NetGear
└── client.py   # Receives frames and runs object detection
````

---

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install vidgear[asyncio] opencv-python gluoncv mxnet
```

> Note: You may need `mxnet-cu113` or other versions depending on your GPU.

### 2. Run Server

```bash
python server.py
```

Make sure `streetvideo.mp4` or another video is available in the working directory.

### 3. Run Client

In another terminal:

```bash
python client.py
```


---

## 🧠 Model Used

* `ssd_512_mobilenet1.0_voc_int8`
* Pre-trained on PASCAL VOC
* Hybridized with static shapes for performance

---

## 💬 Notes

* The `server.py` uses JPEG compression settings (commented out) which can be enabled for better performance over slow networks.
* This project is for experimentation with Vidgear and GluonCV; adapt it for production use with proper error handling, multi-threading, and graceful exits.

---

## 🛠️ Acknowledgements

* [VidGear](https://github.com/abhiTronix/vidgear) – high-performance video-processing Python library
* [GluonCV](https://cv.gluon.ai/) – toolkit for deep learning in computer vision

---

## 📜 License

This project is released under the [MIT License](LICENSE).
