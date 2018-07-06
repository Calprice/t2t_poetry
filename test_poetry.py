from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import re

books = [# bookid, skip N lines
    (19221, 223), (15553, 522)]

with open('data/poetry/raw.txt', 'w') as ofp:
    for (id_nr, toskip) in books:
        text = strip_headers(load_etext(id_nr)).strip()
        lines = text.split('\n')[toskip:]
        for line in lines:
            if len(line) > 0 and line.upper() != line:
                # The below changes into a space anything that is not a lowercase letter, a ' and a -
                cleaned = re.sub('[^a-z\'\-]+', ' ', line.strip().lower())
                ofp.write(cleaned + '\n')
            else:
                ofp.write('\n')

with open('data/poetry/raw.txt', 'r') as rawfp, open('data/poetry/input.txt', 'w') as infp, open(
    'data/poetry/output.txt', 'w') as outfp:
    prev_line = ''
    for curr_line in rawfp:
        curr_line = curr_line.strip()
        # poems break at empty lines, so this ensures we train only
        # on lines of the same poem
        if len(prev_line) > 0 and len(curr_line) > 0:
            infp.write(prev_line + '\n')
            outfp.write(curr_line + '\n')
        prev_line = curr_line