from __future__ import absolute_import, division, print_function, unicode_literals

import pi3d

#Display class is the core of pi3d, used to hold screen info
#Shape class - all drawn objects in pi3d inherit from the Shape class.
#Buffer objecft - contains arrays of values representing vertices.
#Shader class - used to compile very fast programs 
#Camera
#Texture objects - used to load images
#Light

#create screen
display = pi3d.Display.create()
display.set_background(0.0, 0.0, 0.0, 1)

#create shader
shader = pi3d.Shader("uv_light")
earth_texture = pi3d.Texture("earthtexture.jpg")

ball = pi3d.Sphere(z = 5.0)  
#ball.set_material((1.0,0,0,0,0)) #change ball color

#listen for keystrokes
mykeys = pi3d.Keyboard()

while display.loop_running():
	k = mykeys.read()
	if k == 27:
		#esc
		mykeys.close()
		display.destroy()
		break
	ball.draw(shader, [earth_texture])
	
