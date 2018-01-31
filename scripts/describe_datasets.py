import glob, pandas as pd

setlength = lambda fn: sum([len(df) for df in pd.read_csv(fn, chunksize=100000)])
	
if __name__ == '__main__':
	for fn in glob.glob('*.csv.gz'):
		print(fn, setlength(fn))