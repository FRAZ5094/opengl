import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("glfw can not be initialized")

#create window
window = glfw.create_window(960,1080,"My OpenGL window", None,None)

#check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window cannot be created")


#set windows position
#glfw.set_window_pos(window,400,200)

#make the context current
glfw.make_context_current(window)

# x,y,z,x,y,z,x,y,z
verticies=[-0.5,-0.5,0.0, 
            0.5,-0.5,0.0, 
            0.0,0.5,0.0]


#r,b,g,r,b,g,r,g,b
colors=[1.0,0.0,0.0,
        0.0,1.0,0.0,
        0.0,0.0,1.0]

verticies=np.array(verticies, dtype=np.float32)
colors=np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
#3 vertexes
glVertexPointer(3,GL_FLOAT,0,verticies)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3,GL_FLOAT,0,colors)

glClearColor(0,0.1,0.1,1)

#main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    ct=glfw.get_time() #time from start of program

    #2 deg per loop, and in y axis
#    glRotatef(2,1,1,0)
    glTranslatef(0.01*np.sin(ct),0,0)

    glDrawArrays(GL_TRIANGLES,0,3)

    glfw.swap_buffers(window)

glfw.terminate()
