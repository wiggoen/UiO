FYS3150/FYS4150 - Project 3 Building a model for the solar system using ordinary differential equations
============

By default, the program prints all positions every timestep to a file called positions.xyz. You can visualize this by using i.e. [Ovito](http://ovito.org/). 

You can choose if you want to run the program from either C++ or Python. 

Default setup in C++ program:
* numTimesteps = 1000             (Number of timesteps)
* dt = 0.001                      (Distance between timesteps)
* outputmode = "Ovito"            (Use "Ovito" or "Python" for wrinting to file)
* outfilename = "positions.xyz"       (The output file name of your choice. Use .xyz for use with Ovito)
* integrator = "Verlet"           (Use "Verlet" or "Euler")
* system = "Sun-Earth"            (Use "Sun-Earth", "Planet-Escape", "Sun-Mercury", "Sun-Mercury-GR", "Sun-Earth-Jupiter" or "System-without-GR")
* printEvery = 1                  (Writes every number of steps of your choice. "1" means every timestep. If you use 100000 timesteps for i.e. "System-without-GR", the output file will be approximately 50 MB. 'GitHub will warn you when pushing files larger than 50 MB. You will not be allowed to push files larger than 100 MB.' So if you want to use more than 100000 timesteps you should consider printing i.e. every 500 timesteps to reduce the file size.)

Default setup in Python file 'Project_3.py':
The default setup in Python are mainly the same, but there are a few differences:
* outfilemode = "Python"          (This is because the Python program plots directly using matplotlib.)
* optimization_flag = "-O0"       (When running from Python you can set an optimization flag before you run the code. Default is "-O0" (no flag), but you can change it to i.e. "-O3" if you want your compiler to optimize the running of the code.)

Python files:
* 'Python_3_runtimes.py' calculates the runtimes for different values of timesteps, integrators and optimization flags. 
* 'Project_3_SE_special.py' plots the Sun and the Earth for calculated positions with Sun-Earth system and Sun-Earth-Jupiter system.
* 'Project_3_dt_special.py' plots the Sun-Earth system with 10000 timesteps and different dt's. 
* 'Project_3_Mercury.py' plots the perihelion precession of Mercury. 

The systems:
* "Sun-Earth" gives the Earth orbiting the Sun.
* "Planet-Escape" gives a planet in distance 1 AU (like the Earth) having enough velocity to ecape from the Suns gravity.
* "Sun-Mercury" gives Mercury orbiting the Sun.
* "Sun-Mercury-GR" gives Mercury orbiting the Sun by calculating general relativity.
* "Sun-Earth-Jupiter" gives the Earth and Jupiter orbiting the Sun.
* "System-without-GR" gives the solar system (with Pluto).
* "System-runtime" is run by 'Project_3_runtimes.py' and calculates runtimes for the algorithms. 
