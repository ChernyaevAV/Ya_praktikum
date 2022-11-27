from typing import Optional, List

homes_list = [0, 1, 2, 0, 4]

zero_idx: Optional[int] = None
res: List[int] = [0] * len(homes_list)
for idx, house_num in enumerate(homes_list):
    if house_num == 0:
        if zero_idx is None:
            res[0:idx] = res[0:idx][::-1]
        else:
            node_idx, rem = divmod(idx + zero_idx, 2)
            res[node_idx + 1: idx] = res[zero_idx + 1:node_idx + rem][::-1]
        zero_idx = idx
    else:
        res[idx] = idx + 1 if zero_idx is None else idx - zero_idx
    print(res)

