import glob
from google.colab import files
uploaded = files.upload()
for filename in glob.glob('*'):
  print(filename)