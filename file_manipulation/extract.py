def extract(path = '/squids_tmp/batman-adv-2015.1.tar.gz'):
	'''Extract a tar file.

	ARGS:
	@path -- The absolute path to the tar file as a STRING

	RETURN:
	None
	'''
	import tarfile
	tar = tarfile.open(bat_path)
	tar.extractall()
	tar.close()

if __name__ == '__main__':
	import argparse
	parser = ArgumentParser()
	parser.add_argument('path', default = '/squids_tmp/batman-adv-2015.1.tar.gz')
	args = parser.parse_args()

	extract(args.path)
