from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# elem_list = []
for elem in ft_tqdm(range(333)):
    # elem_list.append(elem)
    sleep(0.005)
# print(elem_list)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()