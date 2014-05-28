# DataMiningTechniques

Data Mining Techniques

## Setup

Python version 3 needs to be installed on the local system

The following packages are required for running most the scripts:

 * numpy
 * scipy
 * matplotlib

If those packages are installed, then ``pylab`` will be available on the system. Remember to install
the specific versions for Python version 3.

### In Ubuntu

    sudo apt-get install python3-numpy python3-scipy python3-matplotlib

### In Windows
    
Since some additional packages are required, [Conda](http://conda.pydata.org/index.html) is a good choice helps to manage different version of python and packages easily. Installers can be found [here](http://conda.pydata.org/miniconda.html).

After installation, use conda command to install these packages:

* numpy
* matplotlib
* scipy

Here's the command (It's in system command-line, not in python's):
    
    conda install numpy matplotlib scipy pandas

## Running

### In Ubuntu

    python3 ./run.py <command>

### In Windows

    python run.py <command>

Where ``<command>`` might be one of the following:

* ``ratiocharts``, which creates pie plots
* ``header``, which displays the dataset's fields
* ``row <n>``, which displays the ``<n>``-th row
