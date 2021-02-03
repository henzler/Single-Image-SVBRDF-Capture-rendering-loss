This document provides a quick explanation on how to use the inference code "material_net_test.py".

LICENSE:
For research only, not for commercial use. Do not distribute
Data was generated using Substance Designer and Substance Share library : https://share.allegorithmic.com

Attention: This is a temporary license, detailed version will be available soon, please come back soon

Please contact valentin.deschaintre@inria.fr for any question (inria and Optis for Ansys collaboration).

INPUT-OUTPUTS:
This code takes pictures of material taken with a cellphone (Fov ~ 45 °) and flash approximately in the middle (be careful not to entirerly burn the picture on very specular materials).
It outputs a set of 4 maps (diffuse, specular, roughness and normal) corresponding to a Cook-Torrance GGX implementation.

PRE-REQUISITE(install):

Python (including numpy)
Tensorflow 1.X or 2.X (tested on 1.4, 1.12.1, 2.1.0)
/!\ Uncomment 2 lines at the very top of the code file to run this with TF 2.0+ /!\

Run the test folder:
python material_net_test.py --input_dir inputExamples/ --mode eval --output_dir results --checkpoint ./ --imageFormat png --scale_size 256

HOW TO USE:

Run it as a python script in a command invite:

python material_net_test.py --input_dir $INPUT_DIR --mode eval --output_dir $OUTPUT_DIR --checkpoint $CHECKPOINT_LOCATION --imageFormat $YOURIMAGEFORMAT --scale_size $SIZEOFIMAGESIDE

These are the most interesting parameters. 


Here is a description of all useful parameters for inference :

--input_dir	help="path to xml file, folder or image (defined by --imageFormat) containing information images"
--mode	 required=True  choices=["test", "eval"])   help="Defines the mode of inference (test expect inputs with ground truth, eval expect single pictures )
--output_dir	 required=True, help="where to put output files"
--checkpoint	 required=True, default=None, help="directory with checkpoint to use for testing "
--testMode	 type=str, default="auto"	 choices=["auto", "xml", "folder", "image"], help="What kind of input should be used (auto should automatically determine)"
--imageFormat	 type=str, default="png	 choices=["jpg", "png", "jpeg", "JPG", "JPEG", "PNG"], help="Which format have the input files"
--batch_size	 type=int, default=1, help="number of images in batch to process parallely"
--scale_size	 type=int, default=288, help="scale images to this size before cropping to 256x256. Should be used carefully, it's best to use the actual size of your images here"
--logOutputAlbedos	"Log the output albedos diffuse and specular default is false, to use just add "--logOutputAlbedos""


