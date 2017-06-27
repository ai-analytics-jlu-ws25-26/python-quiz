import glob
import subprocess

files = glob.glob("task*py")
score = -1
for f in files:
    print("%s:" % (f))
    try:
        o = subprocess.check_output("python -m doctest -v %s" % f)
        # print o  # debug info
        score += 1
    except subprocess.CalledProcessError:
        pass

print("Your score is: %d/%d" % (score, len(files) - 1))
