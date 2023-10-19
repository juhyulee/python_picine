from time import sleep

def ft_tqdm(lst: range):
	for idx, value in enumerate(lst):
		print(f"\r{int(value / len(lst) * 101)}%|{'█' * int(value / len(lst) * 130):129}| {idx + 1}/{len(lst)}", end=" ")
		yield value
