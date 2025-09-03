# Python Quiz

This repository contains 10 small Python programming tasks designed to help you assess your Python programming skills. Most tasks are entry-level, while some require intermediate knowledge of Python.

These tasks serve as a self-assessment tool to evaluate your proficiency in Python. All tasks can be solved using Python's standard library, without requiring any third-party libraries. You are encouraged to consult package documentation, visit [Stack Overflow](https://stackoverflow.com/questions), or use Generative AI tools to clarify any questions you encounter while solving the tasks. However, avoid using Generative AI to directly solve the tasks for you—that would defeat the purpose of self-assessment. 😉

The file [task0.py](task0.py) is provided as an example to illustrate how to approach and solve the tasks.

Once you have completed all the tasks, run the following command in your terminal to grade your solutions:
```
streamlit run grader.py
```
## Technical Setup-up
Please follow the steps below to get started with the course material:

1. Install [Python 3.12](https://www.python.org/downloads/release/python-3120/) (or higher) on your local machine.
2. Install [Git](https://git-scm.com/downloads) on your local machine.
3. Clone the repository on your local machine using Git:
    ```
    git clone https://github.com/ai-analytics-jlu-ws25-26/python-quiz.git
    ```
4. Open a terminal in the `.\python-quiz` directory and create a virtual environment:
    ```
    python -m venv .venv
    ```
5. Activate the newly created virtual environment:
    - On Windows:
      ```
      .venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source .venv/bin/activate
      ```
6. Install all required dependencies from the root directory:
    ```
    pip install -r requirements.txt
    ```
7. Open Jupyter Lab:
    ```
    jupyter lab
    ```

## Notes

- The grading system uses Python's doctest module to evaluate your solutions.
- Make sure your solutions are saved in files named task*.py (e.g., task0.py, task1.py).
- Have fun solving the tasks and testing your Python skills!


Feel free to reach out if you encounter any issues or have questions about the tasks. 

