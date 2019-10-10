import glob
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.join(dir_path, "inference", "siammask_sharp"))
sys.path.insert(2, os.path.join(dir_path, "inference"))
from test import *
from custom import Custom
import requests
from tqdm import tqdm
import math

class tracking():

    def __init__(self, model_name):

        model_path = os.path.join(dir_path, "siammask_sharp", model_name+".pth")
        if not os.path.exists(model_path):
            path_to_save = os.path.join(dir_path, "siammask_sharp")
            url = "http://www.robots.ox.ac.uk/~qwang/"+model_name+".pth"
            self.download_file(url, path_to_save)
            self.path_to_davis = model_path
        else:
            self.path_to_davis = model_path

        short_model_name = model_name.split("_")[-1].lower()

        config_path = os.path.join(dir_path, "siammask_sharp", "config_"+short_model_name+".json")
        self.path_to_config = config_path

    def download_file(self, url, path_to_save):
        """
        This function is used to download a file from url with progress bar.
        Args:
            url {str}: http link to the file to download
            path_to_save {str}: folder path where the urls data is to be saved.
        Returns {str}: absolute path to image urls data.
        """
        local_filename = os.path.join(path_to_save, url.split('/')[-1])
        # NOTE the stream=True parameter below
        with requests.get(url, stream=False) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 8192
            with open(local_filename, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=block_size), total=math.ceil(total_size // block_size),unit='KB', unit_scale=True):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
        return local_filename

    def siam_mask_inference(self, path_to_image, bbox):
        parser = argparse.ArgumentParser(description='PyTorch Tracking Demo')

        parser.add_argument('--resume', default=self.path_to_davis, type=str, required=False,
                            metavar='PATH',help='path to latest checkpoint (default: none)')
        parser.add_argument('--config', dest='config', default=self.path_to_config,
                            help='hyper-parameter of SiamMask in json format')
        parser.add_argument('--base_path', default=path_to_image, help='datasets')
        parser.add_argument('--cpu', action='store_true', help='cpu mode')
        args = parser.parse_args()

        # Setup device
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        torch.backends.cudnn.benchmark = True

        # Setup Model
        cfg = load_config(args)
        siammask = Custom(anchors=cfg['anchors'])
        if args.resume:
            assert isfile(args.resume), 'Please download {} first.'.format(args.resume)
            siammask = load_pretrain(siammask, args.resume)
        siammask.eval().to(device)

        # Parse Image file
        ims = cv2.imread(path_to_image)
        x, y, w, h = bbox

        target_pos = np.array([x + w / 2, y + h / 2])
        target_sz = np.array([w, h])
        state = siamese_init(ims, target_pos, target_sz, siammask, cfg['hp'], device=device)  # init tracker
        state2 = siamese_track(state, ims, mask_enable=True, refine_enable=True, device=device)  # track
        location = state2['ploygon'].flatten()

        x1, y1 = int(location[0]), int(location[1])
        x2, y2 = int(location[2]), int(location[3])
        x3, y3 = int(location[4]), int(location[5])
        x4, y4 = int(location[6]), int(location[7])

        # cv2.polylines(ims, [np.int0(location).reshape((-1, 1, 2))], True, (0, 255, 0), 3)
        # cv2.circle(ims, (x1, y1), 3, (0, 0, 255), -1)
        # cv2.circle(ims, (x2, y2), 3, (0, 0, 255), -1)
        # cv2.circle(ims, (x3, y3), 3, (0, 0, 255), -1)
        # cv2.circle(ims, (x4, y4), 3, (0, 0, 255), -1)
        #
        # cv2.imshow('SiamMask', ims)
        # cv2.waitKey(0)

        return (x1, y1), (x2, y2), (x3, y3), (x4, y4 )


