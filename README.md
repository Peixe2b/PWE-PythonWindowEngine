<div align="center">
  <img width="172" height="151" src="https://private-user-images.githubusercontent.com/109036036/405786567-6d311385-93b0-4acc-90dd-360c8155acb9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc1ODAxNjQsIm5iZiI6MTczNzU3OTg2NCwicGF0aCI6Ii8xMDkwMzYwMzYvNDA1Nzg2NTY3LTZkMzExMzg1LTkzYjAtNGFjYy05MGRkLTM2MGM4MTU1YWNiOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyMlQyMTA0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05M2YyN2QxNWE5NTQ2MDlhZGIwNTcwMzIzNjc2YzA5OTJlYmU2N2VlNGFmZmJmNmMyODEwMzZhZTJkNzY3NTcyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9OWEhIu18zhkDIBXl0S43jpF1nMaVqvxhuFO-3NrTh0">

  <h1>PWE</h1>
  A simple but efficient game framework

  <a href="#about">About</a> • 
  <a href="#todo">Todo</a> • 
  <a href="#suport">Suport</a> • 
  <a href="#installation">Installation</a> • 
  <a href="#use">Use</a> •
  <a href="#documentation">Documentation</a>
</div>

<hr>

### ABOUT
**PWE** is a simple and python game framework for creating games for desktop.

<hr>

### TODO
  - [ ] Window Creation
  - [ ] Update and Draw
  - [ ] Window management
  - [ ] Map Editor
  - [ ] Sprite Editor
  - [ ] Texture
  - [ ] Audio
  - [x] Error handling
  - [ ] Game state manager  
  - [ ] Component creation
  - [ ] GameTimer and Clock
  - [ ] IO
  - [ ] Animator system
  - [ ] Event manager
  - [ ] Keyboard and mouse input
  - [ ] Logger
  - [ ] Connections with other APIs
    - [ ] OpenGL
    - [ ] CUDA
    - [ ] STB
    - [ ] OpenAL
    - [ ] SDL2
    - [ ] PIL
  - [ ] GUI

<hr>

### SUPORT
**PWE** supports connections with desktop Linux.

 * Linux
    * Bothi Linux
    * Linux Mint 22
    * MiniOS

<hr>

### INSTALLATION
The installation is different for each operating system, but simple to execute. For now, PWE only works on Linux, but in the future, we will extend it to macOS.

#### Linux
Use the command below to install SDL2.

```bash
sudo apt-get install libsdl2-dev
```

When you install SDL2, you can install PyPy 7.x to improve the performance of your game, as PyPy provides JIT compilation, being much more efficient compared to CPython. PWE works the same way in both compilers

<hr>

### USE
After the installation, let's create a window! It's very simple to create a window in PWE.

```python
from PWE import * # Import PWE
from time import sleep

PWE_Init() # Initialize system
window = PWE_CreateWindow("MyGame", 800, 500) # Create a simple window

if window is None: # Verify if window is None
    raise OSError()

surface = PWE_GetSurface(window)

PWE_UpdateWindow(window)
sleep(5) # Sleep for 5 seconds

PWE_Terminate() # Clean up
```

<hr>

### DOCUMENTATION

We are developing documentation and fixing errors related to the lib. The documentation is being written from the 'docs' of PWE. If you want to contribute, just send a pull request to us.