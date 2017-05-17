import glob
import subprocess

files = glob.glob("task*py")
score = 0
for f in files:
	try:
		o = subprocess.check_output("python -m doctest -v %s" % f)
		score += 1
	except subprocess.CalledProcessError:
		pass

print("Your score is: %d/%d" % (score,len(files)))
