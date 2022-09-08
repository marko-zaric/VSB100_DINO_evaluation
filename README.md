# Evaluation of DINO on VSB100

## Overview

Vision Transformers can be trained in a self-supervised manner using the DINO (knowledge
distillation with no labels) approach. The model can then be applied to various problems, such
as video instance segmentation. In this study, we further evaluate the performance of DINO for
video instance segmentation by expanding the evaluation by the VSB100 dataset. We find that
the performance is highly dependent on the preprocessing steps and that the out-of-the-box DINO
video segmentation still performs well on a dataset with significantly more trackable objects per
video frame but suffers from a performance loss of around 10 percentage points compared to the
DAVIS-2017 evaluation. 

## Preprocessing

In order to provide a tractable comparison between the DAVIS-2017 dataset used to evaluate video segmentation in
the original paper and our evaluation, the VSB100 dataset was preprocessed to resemble DAVIS-2017 at least in a
dimensional sense. The first step was to resize the original images and annotations to match the 1152 × 480 format.
In this context, a mask is a distinct color in an annotation image that groups objects or areas into colors. One big
difference between DAVIS-2017 and VSB100 is that DAVIS-2017 has at most 5 masks per video, focusing only on
the most prominent objects in the frame and leaving a lot of space blacked out. Blacked-out space is ignored during
evaluation. VSB100, on the other hand, often has up to 20 masks annotating every detail in the scene, leaving nothing
unannotated. This caused issues in the evaluation when the code tried to allocate a large multidimensional array which
quickly caused memory issues. To counter this, we used the python package Pillow to extract the most quantitatively
represented colors and restrict the number of masks to 5.

## Evaluation Setup

For the evaluation step, we followed the instructions on the original paper step by step for evaluating video object
segmentation. We used a pretrained version of ViT-S/16. In the first step, DINO is used to generate the segmentation in a
semi-supervised manner using the script *eval_video_segmentation.py*. The newly generated segmentation is then
evaluated using the DAVIS-2017 evaluation which is publicly available. To be able to use the *evaluation_method.py*
out of the box, we adjusted the folder structure of our annotations and images to match that of the DAVIS-2017.
To get results comparable to those from the original paper, we employ the same metrics: the mean region similarity Jm and the mean
contour-based accuracy Fm. 

## Results

The main goal of our work was to reproduce the good results in video segmentation shown by DINO in their original
paper with a different and for DINO unseen dataset. Table 1 shows the results on both the DAVIS-2017 and VSB100
datasets. In both cases, the used model is ViT-S/16.

|              | Jm        | Fm         |  (J & F)m   |
|--------------|-----------|------------| ------------|
| DAVIS-2017   | 60.2      | 63.4       | 61.8        |
| VSB100       | 49.0      | 52.0       | 50.5        |

It is worth keeping in mind, however, that the provided evaluation method was specifically designed to evaluate the
DAVIS-2017 dataset, which only uses relatively few masks per frame, compared to VSB100. Therefore, the results
shown in table 1 are impressive.
While examining the performance metrics for each set of frames individually, the main performance damper for our
method of evaluation is easily uncovered. Since we had to reduce the number of masks for the VSB100 dataset in order
to use the same evaluation methods as Caron et al., we work with the assumption that similar colors can be merged.
However, this created issues, especially for sets of frames with many small masks.
