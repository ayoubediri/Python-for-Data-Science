from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(100)):
    sleep(0.1)
print()
for elem in tqdm(range(100)):
    sleep(0.1)
print()