import os
import re
import sys

git_dir = sys.argv[1]
dest_dir = sys.argv[2]

# Match the hash values
sha1num_re = re.compile(r"[a-z0-9]{40}")
# Match filenames
filename_re = re.compile(r"name = \.?\b\w+[./\w+]*\b")

# Get the contents of .git/index
index = os.popen('gin ' + git_dir + '/index', 'r').read()

sha1nums = sha1num_re.findall(index)
# To remove the redundant checksum
sha1nums.pop(-1)
filenames = filename_re.findall(index)

shas = []
for sha1num in sha1nums:
	# To match objects more easily
	shas.append(sha1num[-6:])


files = []
for filename in filenames:
	files.append(filename[7:])
	# Use advance-touch to create files along with directories
	os.system('ad ' + dest_dir + '/' + filename[7:])

# Dict for matching
sha1_file_dict = dict(zip(shas, files))

objects = os.popen("find ./objects -type f", 'r').read().split("\n")

# Remove empty values
objects = list(filter(None, objects))

for obj in objects:
	if obj[-6:] in sha1_file_dict:
		# Use zpipe to get file contents
		raw_contents = os.popen('./zpipe -d < ' + obj).read()
		with open(dest_dir + '/' + sha1_file_dict[obj[-6:]], 'w') as f:
			# Remove the `\x00` between contents and length value
			file_contents = str(raw_contents).partition('\x00')[2].strip()
			f.write(str(file_contents))
