from pathlib import Path
import json
from subprocess import call

dataset_dir = '/home/henzler/share/datasets/neuraltexture/flash_images'
output_path = '../results/valentin'

with open(str(Path(dataset_dir, 'metadata.json')), 'r') as f:
    metadata = json.load(f)

    materials = metadata['materials']

    samples = []
    for material in materials:

        material_id = material['material_id']

        if material['split'] != 'test' and not material_id == '1847' \
                and not material_id == '1848' and not material_id == '1886' \
                and not material_id == '1906':
            continue

        idx = material['material_id']

        entry = material['entries'][0]
        filename = '{}{}'.format(entry['name'], entry['suffix'])

        input_dir = str(Path(dataset_dir, material['split'], idx, filename))
        output_dir = Path(output_path, idx)

        if output_dir.is_dir():
            print('Skip', str(output_dir))
            continue
        else:
            output_dir.mkdir(exist_ok=True,parents=True)

        call('python material_net.py '
                  '--input_dir {} '
                  '--mode eval '
                  '--checkpoint . '
                  '--batch_size 1 '
                  '--scale_size 512 '
                  '--correctGamma '
                  '--output_dir {}'
                  .format(
                    str(input_dir),
                    str(output_dir)
        ), shell=True)

