
bar_dict = {
    0 : "▏",
    1 : "▎",
    2 : "▍",
    3 : "▌",
    4 : "▋",
    5 : "▊",
    6 : "▉",
    7 : "█",
}

def ft_print_progres(current: int, total: int, width: int = 172) -> str:
    percent = current / total
    addtion = 100 - (percent * 100)
    total_blocks = width * 8 
    filled = int(percent * total_blocks)
    not_filled = total_blocks - filled
    full = filled // 8
    not_full = not_filled // 8
    remainder = filled % 8
    
    bar = bar_dict[7] * full
    if remainder:
        bar += bar_dict[remainder]
        not_filled -= 1
    if not_filled > 0:
        bar += " " * (not_full)
    return bar
        
        

def ft_tqdm(lst: range):
    len_ = len(lst)
    for i in lst:
        current = i + 1
        percent = (current * 100) // len_
        bar = ft_print_progres(current, len_)
        line = f"{percent:>3}%|{bar}| {current}/{len_}"
        print(f"\r{line}", end="", flush=True)
        yield lst[i]
