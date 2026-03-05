""" 
    a virtual environment is an isolated python environment
    it lets you install packages for one project without effecting others
    useful when different projects need different version of libraries
    "Common tools"
    venv (built in since python 3.3)
    virtualenv (external, older but still used)
    conda (for data science, comes with anaconda)
    
"""
# "Create a virtual environment"
# python -m venv myenv
# this creates a folder myenv with its own python interpreter and libraries

# "Active the environment"
# myenv\Scripts\activate
# you'll see (myenv) before your terminal prompt, meaning it's active

# install packages inside
# pip install requests
# pip install numpy
# these packages are installed only inside myenv, not globally

# deactive 
# deactivate
# this exits the virtual environment



