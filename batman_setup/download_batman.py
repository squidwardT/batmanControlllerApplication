import argparse
from urllib import urlretrieve

from extract import extract

def download_batman(path = '/squids_tmp'):
	'''Download BATMAN-Advanced to the specified PATH and unpack.

	ARGS:
	@path -- The absolute path to the directory in which the package should be placed

	RETURN:
	None
	'''

	bat_path =  path + '/batman-advanced-2015.1.tar.gz'
	urlretrieve('http://downloads.open-mesh.org/batman/stable/sources/batman-adv/batman-adv-2015.1.tar.gz', bat_path)
	extract(bat_path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path', default = '/squids_tmp')
	args = parser.parse_args()

	download_batman(args.path)
