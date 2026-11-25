# Verified: 99 characters (99 UTF-8 bytes), no trailing newline.
LINE = "It was not a bug, it was a feature that escaped. I have filed a missing feature report with myself."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
output_path = os.path.join(output_dir, 'entry.txt') if output_dir else '/output/entry.txt'

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
