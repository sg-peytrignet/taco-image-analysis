import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import skimage

def display_images_with_coco_annotations(image_id_subset, figtitle, dataset_path, annotations, display_type='both', colors=None):
    """
    Function to display images with COCO annotations. Adapted from Dr. Sreenivas Bhattiprolu.

    Parameters:
    - image_id_subset (list): A list of image IDs to display.
    - figtitle (str): Title for the figure.
    - dataset_path (str): Path to the dataset directory.
    - annotations (dict): The dictionary containing COCO annotations data.
    - display_type (str, optional): Type of annotations to display. Options are 'bbox', 'seg', or 'both'. Default is 'both'.
    - colors (list, optional): List of colors for displaying annotations. Default is None.

    Returns:
    - None
    """
    # Subset of images that include the specified type
    subset_files = [os.path.join(dataset_path, img['file_name']) for img in annotations['images'] if img["id"] in image_id_subset]

    # Random subset of 6 images
    random.seed(0)
    image_paths = random.sample(subset_files, min(6,len(image_id_subset)))

    fig, axs = plt.subplots(2, 3, figsize=(6, 4))

    for ax, img_path in zip(axs.ravel(), image_paths):
        # Load image using OpenCV and convert it from BGR to RGB color space
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        ax.imshow(image)
        ax.axis('off')  # Turn off the axes

        # Define a default color map if none is provided
        if colors is None:
            colors = plt.colormaps["tab10"]

        # Get image filename to match with annotations
        path_components = img_path.split("/")
        short_path = "{}/{}".format(path_components[-2],path_components[-1])
        img_id = next(item["id"] for item in annotations['images'] if item["file_name"] == short_path)

        # Filter annotations for the current image
        img_annotations = [ann for ann in annotations['annotations'] if ann['image_id'] == img_id]

        for ann in img_annotations:
            category_id = ann['category_id']
            color = colors(category_id % 10)

            # Display bounding box
            if display_type in ['bbox', 'both']:
                bbox = ann['bbox']
                rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=1, edgecolor=color, facecolor='none')
                ax.add_patch(rect)

            # Display segmentation polygon
            if display_type in ['seg', 'both']:
                for seg in ann['segmentation']:
                    poly = [(seg[i], seg[i+1]) for i in range(0, len(seg), 2)]
                    polygon = patches.Polygon(poly, closed=True, edgecolor=color, fill=False)
                    ax.add_patch(polygon)

    plt.tight_layout(rect=[0, 0, 0.98, 0.98])
    fig.suptitle(figtitle)
    plt.show()

def show_annotation_image(annotation_id, annotations, dataset_path):
    """
    Function to display untransformed images.

    Parameters:
    - annotation_id (int): The ID of the annotation.
    - annotations (dict): The dictionary containing annotations data.

    Returns:
    - numpy.ndarray: The untransformed image in RGB format.
    """
    # Get image id
    image_id = next(annot["image_id"] for annot in annotations['annotations'] if annot["id"] == annotation_id)

    # Get image location
    image_filename = next(img["file_name"] for img in annotations['images'] if img["id"] == image_id)
    image_location = os.path.join(dataset_path, image_filename)

    # Get image
    image_to_show = cv2.imread(image_location)
    image_to_show = cv2.cvtColor(image_to_show, cv2.COLOR_BGR2RGB)

    return image_to_show


def try_square_crop(annotation_id,annotations,widen_param,newsize,dataset_path):
    """
    Function to resize images into standard square sizes,
    so they can be used in machine learning models.

    Parameters:
    - annotation_id (int): The ID of the annotation.
    - annotations (dict): The dictionary containing annotations data.
    - widen_param (float): The parameter to adjust square widening (0 to 1).
    - newsize (int): The desired size of the square image in pixels.

    Returns:
    - numpy.ndarray: The resized square image with borders added if necessary.
    """

    #Fix parameter if a value bigger than 1 is provided
    widen_param = min(1,widen_param)

    #Get image id for the selected annotation
    image_id = next(annot["image_id"] for annot in annotations['annotations'] if annot["id"]==annotation_id)

    #Get image location
    image_filename = next(img["file_name"] for img in annotations['images'] if img["id"]==image_id)
    image_location = os.path.join(dataset_path, image_filename)

    #Get image
    image_to_crop = cv2.imread(image_location)
    image_to_crop = cv2.cvtColor(image_to_crop, cv2.COLOR_BGR2RGB)

    #Get image dimensions
    raw_ymax, raw_xmax, _ = image_to_crop.shape

    #Get bbox for image
    annotation_bbox = next(annot["bbox"] for annot in annotations['annotations'] if annot["id"]==annotation_id)
    square_side = max(annotation_bbox[2],annotation_bbox[3])

    #Get image centroid coordinates
    x_centroid, y_centroid = annotation_bbox[0]+round(annotation_bbox[2]/2,0), annotation_bbox[1]+round(annotation_bbox[3]/2,0)

    #Largest side
    image_side = max(raw_ymax,raw_xmax)
    bbox_side = max(annotation_bbox[2],annotation_bbox[3])
    caliper = 0.5*(square_side + widen_param*(image_side-square_side))

    #Get square coordinates
    y_max, y_min, x_max, x_min  = y_centroid + caliper, y_centroid - caliper, x_centroid + caliper, x_centroid - caliper

    #Adjust if coordinates are outside image and convert to integer
    y_max, y_min, x_max, x_min = int(min(y_max, raw_ymax)), int(max(0,y_min)), int(min(x_max, raw_xmax)), int(max(0,x_min))

    #New image after cropping
    cropped_image = image_to_crop[y_min:y_max,x_min:x_max]

    #Extract height and width of new image
    pre_border_height = cropped_image.shape[0]
    pre_border_width = cropped_image.shape[1]

    #Compute size of borders
    left_right_border = int(max(0,round(0.5*(pre_border_height-pre_border_width),0)))
    top_bottom_border = int(max(0,round(0.5*(pre_border_width-pre_border_height),0)))

    #Add black borders if necessary, to turn into a square
    cropped_image_with_border = cv2.copyMakeBorder(cropped_image, top_bottom_border, top_bottom_border, left_right_border, left_right_border, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    #Resize into a standard size for models
    cropped_image_with_border = cv2.resize(cropped_image_with_border, (newsize, newsize), interpolation= cv2.INTER_LINEAR)

    return cropped_image_with_border


def mask_and_square_crop(annotation_id, annotations, widen_param, newsize, dataset_path):
    """
    Function to create a binary mask for each annotation and resize it according to the same criteria found in the 'try_square_crop' function.

    Parameters:
    - annotation_id (int): The ID of the annotation.
    - annotations (dict): The dictionary containing annotations data.
    - widen_param (float): The parameter to adjust square widening (0 to 1).
    - newsize (int): The desired size of the square image.

    Returns:
    - numpy.ndarray: The resized square binary mask image with borders added if necessary.
    """
    # Fix parameter if a value bigger than 1 is provided
    widen_param = min(1, widen_param)

    # Get image id for the selected annotation
    image_id = next(annot["image_id"] for annot in annotations['annotations'] if annot["id"] == annotation_id)

    # Get image location
    image_filename = next(img["file_name"] for img in annotations['images'] if img["id"] == image_id)
    image_location = os.path.join(dataset_path, image_filename)

    # Get image
    image_to_crop = cv2.imread(image_location)
    image_to_crop = cv2.cvtColor(image_to_crop, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    raw_ymax, raw_xmax, _ = image_to_crop.shape

    # Get segmentation
    seg = next(annot["segmentation"] for annot in annotations['annotations'] if annot["id"] == annotation_id)[0]

    # Create mask
    mask_np = np.zeros((image_to_crop.shape[0], image_to_crop.shape[1]), dtype=np.uint16)
    rr, cc = skimage.draw.polygon(seg[1::2], seg[0::2], mask_np.shape)
    mask_np[rr, cc] = 1

    # Get bbox for image
    annotation_bbox = next(annot["bbox"] for annot in annotations['annotations'] if annot["id"] == annotation_id)
    square_side = max(annotation_bbox[2], annotation_bbox[3])

    # Get image centroidn coordinates
    x_centroid, y_centroid = annotation_bbox[0] + round(annotation_bbox[2] / 2, 0), annotation_bbox[1] + round(
        annotation_bbox[3] / 2, 0)

    # Largest side
    image_side = max(raw_ymax, raw_xmax)
    bbox_side = max(annotation_bbox[2], annotation_bbox[3])
    caliper = 0.5 * (square_side + widen_param * (image_side - square_side))

    # Get square coordinates
    y_max, y_min, x_max, x_min = y_centroid + caliper, y_centroid - caliper, x_centroid + caliper, x_centroid - caliper

    # Adjust if coordinates are outside image and convert to integer
    y_max, y_min, x_max, x_min = int(min(y_max, raw_ymax)), int(max(0, y_min)), int(min(x_max, raw_xmax)), int(
        max(0, x_min))

    # New image after cropping
    cropped_image = mask_np[y_min:y_max, x_min:x_max]

    # Extract height and width of new image
    pre_border_height = cropped_image.shape[0]
    pre_border_width = cropped_image.shape[1]

    # Compute size of borders
    left_right_border = int(max(0, round(0.5 * (pre_border_height - pre_border_width), 0)))
    top_bottom_border = int(max(0, round(0.5 * (pre_border_width - pre_border_height), 0)))

    # Add black borders if necessary, to turn into a square
    cropped_image_with_border = cv2.copyMakeBorder(cropped_image, top_bottom_border, top_bottom_border,
                                                    left_right_border, left_right_border, cv2.BORDER_CONSTANT,
                                                    value=[0, 0, 0])

    # Resize into a standard size for models
    cropped_image_with_border = cv2.resize(cropped_image_with_border, (newsize, newsize),
                                            interpolation=cv2.INTER_LINEAR)

    # Add a dimension
    cropped_image_with_border = cropped_image_with_border.reshape(cropped_image_with_border.shape[0],
                                                                    cropped_image_with_border.shape[1], 1)

    return cropped_image_with_border