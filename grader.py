import streamlit as st
import glob
import subprocess
import re

def run_doctests():
    files = glob.glob("task*py")
    if not files:
        st.warning("No task files found. Please ensure files are named as 'task*.py'.")
        return

    results = []
    total_score = 0

    for f in files:
        try:
            o = subprocess.check_output(("python -m doctest -v %s" % f).split(" "))
        except subprocess.CalledProcessError as e:
            o = e.output

        match = re.search(r"(\d+) passed and (\d+) failed", str(o))
        if not match:
            results.append((f, "Could not parse results", 0))
            continue

        passed = int(match.group(1))
        failed = int(match.group(2))
        if passed + failed == 0:
            results.append((f, "No tests found", 0))
            continue

        score = passed / (passed + failed)
        total_score += score
        results.append((f, f"{passed} passed, {failed} failed", score))

    return results, total_score, len(files)

# Streamlit UI
st.title("Python Quiz Grader")
st.write("This application evaluates your Python tasks and calculates a score.")

if st.button("Run Grading"):
    with st.spinner("Running doctests..."):
        results, total_score, total_files = run_doctests()

    if results:
        st.success("Grading complete!")
        st.subheader("Results:")
        for file, result, score in results:
            st.write(f"**{file}**: {result} | Score: {score:.2f}/1.0")

        st.subheader("Summary:")
        st.write(f"**Total Files Graded**: {total_files}")
        st.write(f"**Total Score**: {total_score:.2f}/{total_files}")
    else:
        st.error("No results to display.")
