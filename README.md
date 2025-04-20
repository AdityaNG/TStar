# TStar: A Unified KeyFrame Searching Framework for Video Question Answering

<p align="center">
  <picture>
      <img src="https://github.com/user-attachments/assets/4ce88690-ebbb-41ab-bdbd-522cb63762db" alt="TStar framework" height="300">
  </picture>
</p>

<p align="center">
    <a href="#"><img src="https://img.shields.io/badge/🔍_Post-7588C0?style=for-the-badge&logoColor=white" alt="Post"></a>
    <a href="https://longvideohaystack.github.io/"><img src="https://img.shields.io/badge/🏠_Project_Page-5B8CD8?style=for-the-badge&logoColor=white" alt="Project Page"></a>
    <a href="https://www.lvhaystackai.com"><img src="https://img.shields.io/badge/🎮_Demo-9E75D8?style=for-the-badge&logoColor=white" alt="Demo"></a>
    <a href="https://huggingface.co/datasets/LVHaystack/LongVideoHaystack"><img src="https://img.shields.io/badge/🗃️_Dataset-5BAAD8?style=for-the-badge&logoColor=white" alt="Dataset"></a>
    <a href="https://arxiv.org/abs/2504.02259"><img src="https://img.shields.io/badge/📄_Paper-D86BDB?style=for-the-badge&logoColor=white" alt="Paper"></a>
</p>

**TStar** is an advanced framework that integrates Keyframe Searching into Vision-Language Models (VLMs), enhancing their performance for extremely long video understandiong tasks. By efficiently identifying relevant frames within videos, TStar improves the ability of state-of-the-art models like LLaVA-oneVision, QWen-VL and GPT-4o to understand and reason over video data.


**2025.4.4 Update:** We’ve shared a compact demo set of TStar outputs [LV-Haystack Tiny (Google Drive)](https://drive.google.com/drive/folders/1ig0XtZqGFYwERkARxCQMqIyKQjrtxcrx?usp=sharing)

**2025.4.4 Update:** We are thrilled to release TStar and LongVideoHaystack!


## Features
- **Iteratively Searching**: Iteratively identifies and focuses on the most relevant visual information in videos based on the question being asked.
- **Plug-in**: Easily integrates various grounding and searching backends.
- **Efficient Video QA**: Combines T* keyframe search with advanced video question answering capabilities.

---

## Getting Started
### Installation

```bash
## Follow docs/installation to implemet Grounding (e.g., LLaVA) and Searching (e.g., YOLO) Function
###  Install Query Grounder Interface(LLaVA or GPT-API) 
### Optional if you test with GPT4o or QWen
git clone https://github.com/LLaVA-VL/LLaVA-NeXT  

### Install Image Scorer Interface e.g., YOLO-WORLD 
### Optional if you test with owl-vit (fast run but lower performance))
git clone --recursive https://github.com/AILab-CVC/YOLO-World.git
```

Environment setup
```
conda create -n tstar python=3.10 -y
conda activate tstar
conda install -c nvidia/label/cuda-12.4.0 cuda-toolkit
conda install pytorch=2.5.1 torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
pip install -r requirements.txt
```

Run on a video
```
export OPENAI_API_KEY=your_openai_api_key

python -m LVHaystackBench.single_run_TStar \
    --video_path "media/forklift_mini.mp4" \
    --question "What is the color forklift driver's shirt?" \
    --options "A) Red\nB) Black\nC) Blue\nD) White"
```

Results:


<img src="assets/search_iterations.gif">


```
2025-04-20 13:51:24,428 [INFO] PyTorch version 2.5.1 available.
2025-04-20 13:51:27,263 [INFO] OWLInterface initialized successfully.
2025-04-20 13:51:30,255 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-04-20 13:51:30,256 [INFO] Target objects: ['forklift driver', 'shirt']
2025-04-20 13:51:30,256 [INFO] Cue objects: ['forklift', 'steering wheel', 'control panel', 'mirror']
Searching Iterations:   6%|████▍                                                                   | 4/65 [00:13<03:24,  3.35s/iter]Warning: Not enough non-zero entries, adjusting probability distribution.
Searching Iterations:   8%|█████▌                                                                  | 5/65 [00:16<03:21,  3.35s/iter]
2025-04-20 13:51:47,116 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_0_at_4.00s.jpg
2025-04-20 13:51:47,116 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_1_at_6.00s.jpg
2025-04-20 13:51:47,117 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_2_at_18.00s.jpg
2025-04-20 13:51:47,117 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_3_at_20.00s.jpg
2025-04-20 13:51:47,118 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_4_at_28.00s.jpg
2025-04-20 13:51:47,119 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_5_at_30.00s.jpg
2025-04-20 13:51:47,119 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_6_at_45.00s.jpg
2025-04-20 13:51:47,120 [INFO] Saved frame to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/frames/frame_7_at_60.00s.jpg
Saved GIF: ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/search_iterations.gif
2025-04-20 13:51:54,191 [INFO] Saved search iterations GIF to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/search_iterations.gif
Plot saved to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/score_distribution.png
2025-04-20 13:51:54,396 [INFO] Score distribution plot saved to ./results/frame_search/forklift_mini/What is the color forklift driver's shirt/score_distribution.png
2025-04-20 13:51:54,396 [INFO] Found 8 frames, timestamps: [4.0, 6.0, 18.0, 20.0, 28.0, 30.0, 45.0, 60.0]
#################### Original Inputs ####################
Input Quetion: What is the color forklift driver's shirt?
Input Options: A) Red\nB) Black\nC) Blue\nD) White
#################### T* Searching Results ####################
Grounding Objects: target_objects: ['forklift driver', 'shirt'], cue_objects: ['forklift', 'steering wheel', 'control panel', 'mirror']
Frame Timestamps: [4.0, 6.0, 18.0, 20.0, 28.0, 30.0, 45.0, 60.0]
Processed Video Path: media/forklift_mini.mp4
Results:
{
    "video_path": "media/forklift_mini.mp4",
    "grounding_objects": {
        "target_objects": [
            "forklift driver",
            "shirt"
        ],
        "cue_objects": [
            "forklift",
            "steering wheel",
            "control panel",
            "mirror"
        ]
    },
    "keyframe_timestamps": [
        4.0,
        6.0,
        18.0,
        20.0,
        28.0,
        30.0,
        45.0,
        60.0
    ],
    "keyframe_distribution": [
        0.01530221096773617,
        0.015308537995638149,
        0.015314750712846577,
        ...
        0.015321293611050668,
        0.015312678687498466,
        0.01530369160273748
    ]
}
```

### Structure:
```bash
LV-Haystack/
├── LLaVA-NeXT/                # Query grounding and QA interface (e.g., LLaVA or GPT-4 API, or QWen from HF)
├── YOLO-World/                # Object detection model with open vocabulary (optional)
├── TStar/                     # Core Python module for T* keyframe search 
│   ├── interface_grounding.py       # Interface for grounding questions with VLMs
│   ├── interface_heuristic.py      # Function for scoring images using YOLO
│   ├── interface_searcher.py  # Logic for searching keyframes in T*
│   ├── TStarFramework.py      # Example class integrating T* searching with QA
├── LVHaystackBench              # Scripts for inference on the LV-Haystack dataset
│   ├── run_TStar_onDataset.py # Run keyframe search on a given dataset (e.g., LongVideoBench)
│   ├── val_tstar_results.py     # Evaluate keyframe search results on LV-Haystack
│   ├── val_qa_results.py      # Evaluate video question answering with searched keyframes
├── README.md                  # Documentation for the repository


```

## Run TStar Demo

The example below demonstrates how to perform video question answering with keyframe searching framework. This example uses GPT-4o as the VLM and YOLO-World as scoring function.

```python
export OPENAI_API_KEY=your_openai_api_key

python run_TStar_Demo_onVideo.py \
    --video_path /path/to/LVHaystack/38737402-19bd-4689-9e74-3af391b15feb.mp4 \
    --question "What is the color of the couch?" \
    --options "A) Red, B) Blue, C) Green, D) Yellow" \
    --grounder gpt-4o \
    --heuristic owl-vit \
    --search_nframes 8
```

## Test on LV-HayStack
To evaluate T* on a dataset (e.g., LV-Haystack), use the following command:

```bash
bash ./eval_LV_Haystack.sh
```
</details>



### Running T* on Your Dataset

To process your own dataset with T*, you need to prepare a JSON file describing the dataset. The JSON file should follow the format below:
<details>
  <summary>Click to expand JSON examples!</summary>
  
```bash
[
    {
        "file_name": "example_video.mp4",
        "question": "What is the color of the couch?",
        "choices": {
            "A": "Red",
            "B": "Blue",
            "C": "Green",
            "D": "Yellow"
        },
        "frame_indexes": [10, 50, 100]  // Optional: Use this for specific frame sampling
    },
    {
        "file_name": "another_video.mp4",
        "question": "What object is next to the chair?",
        "choices": {
            "A": "Table",
            "B": "Lamp",
            "C": "Sofa",
            "D": "Bookshelf"
        }
    }
]
```
</details>

Once your dataset is prepared, you can run TStar to perform keyframe searching. Use the following command:

<details>
  <summary>Click to expand python script!</summary>
  
```python
python ./run_TStar_onDataset.py \
    --dataset_meta LVHaystack/LongVideoHaystack \
    --split test_tiny \
    --video_root ./Datasets/ego4d_data/ego4d_data/v1/256p \
    --output_json_name TStar_LVHaystack_tiny.json \
    --grounder gpt-4o \
    --heuristic owl-vit \
    --search_nframes 8
# new you have add predict frame index in your annotations json
# and sampine frame with the T* prediction for your works!

```
</details>

# Contact
- Jinhui Ye: jinhuiyes@gmail.com
- Zihan Wang: zihanw@u.northwestern.edu
- Haosen Sun: haosensun2026@u.northwestern.edu
- Keshigeyan Chandrasegaran: keshik@stanford.edu
- Anabella Aisaro: anabellaisaro2025@u.northwestern.edu
- Manling Li: manling.li@northwestern.edu

# Citation
If you find **TStar** helpful, please consider citing us:

```bibtex
@misc{tstar,
      title={Re-thinking Temporal Search for Long-Form Video Understanding}, 
      author={Jinhui Ye and Zihan Wang and Haosen Sun and Keshigeyan Chandrasegaran and Zane Durante and Cristobal Eyzaguirre and Yonatan Bisk and Juan Carlos Niebles and Ehsan Adeli and Li Fei-Fei and Jiajun Wu and Manling Li},
      year={2025},
      eprint={2504.02259},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.02259}, 
}
```
