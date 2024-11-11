from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random
gui = Tk()
gui.title('Pop Cat love Fish')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

run_time=15 #running time (default as 20s)
fps=25
add_fish_period=2#add a fish periodically (every 2 seconds)
add_fish_frame=add_fish_period*fps#which frame to add fish
sleep_time=1/fps*0.7#sleep time fix to 0.7 to give time for canvas update
total_frames=run_time*fps#total frames iterated
MOUSE_CLICK = '<Button-1>'
MOUSE_RELEASE = '<ButtonRelease-1>'
RIGHT_CLICK = '<Button-3>'
MOUSE_WHEEL_MOTION='<B2-Motion>'
MOUSE_WHEEL_CLICK='<Button-2>'
DOUBLE_CLICK='<Double-Button-2>'#Double mouse wheel click
no_fish=random.randint(5,10)#number of fishes initialized (random range from 5-10)
no_watergrass=random.randint(5,10)#number of watergrass initialized (random range from 5-10)
fish_startx=[]#Record the x position of fish
fish_starty=[]#Record the y position of fish
fish_head=[]#Record the heading of the fish i.e. left/right
fish_color=[]#Record the color of fish
fish_size=[]#Record the size of fish
fish_alive=[]#Record the aliveness of fish
land_x=[]#Record the x position of land features(watergrass)
land_y=[]#Record the y position of land features(watergrass)
land_size=[]#Record the size of land features(watergrass)
active_tag=None#tag for active 
delete_tag=None#tag for delete
eat_tag=None#tag for eating
colors=['green','orange','coral','yellow','brown','lightblue','pink','aqua','lightgray','snow']#fish color list, for random selection later
size_of_fish=[100,125,150,175]#fish size list, for random selection later
cat_width=100#car width, initialized as 100 pixels
fish_eaten=0#how many fish eaten by cat
def cat_grow(fish_eaten_size):
    #Grow cat body size and updtae number of fishes cat eaten.
    global cat_width
    global fish_eaten
    cat_width=cat_width+fish_eaten_size/10
    fish_eaten+=1
    
def draw_bg():
    #Draw background. I dont know if there is an inbuilt gradient color options for Tkinter, so I figured to build my own by drawing blocks with different colors.
    #References:
    #1. python hex to int: https://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
    #2. python int to hex: https://stackoverflow.com/questions/35881968/python3-convert-one-int-to-hex

    bg_color="#00FFFF" #Start with sky blue or any other color, finally to pure blue i.e. #0000FF
    gap=10 #block height or so called gap
    n=window_height/gap #how many columns in total for the blocks. 
    R_diff=round(int(bg_color[1:3],16)/n)#How many R values of the color shall changed. 
    G_diff=round(int(bg_color[3:5],16)/n)#How many G values of the color shall changed.
    B_diff=round((255-int(bg_color[5:7],16))/n)#How many B values of the color shall changed.
    for y in range(0,window_height,gap):
        canvas.create_rectangle(0,y,window_width,y+gap,fill=bg_color,outline=bg_color,tag='ocean')
        R=hex(abs(int(bg_color[1:3],16)-R_diff))
        if len(R)==3:
            R='0'+R[2]
        else:
            R=R[2:4]
        G=hex(abs(int(bg_color[3:5],16)-G_diff))
        if len(G)==3:
            G='0'+G[2]
        else:
            G=G[2:4]
        B=hex(abs(int(bg_color[5:7],16)+B_diff))
        if len(B)==3:
            B='0'+B[2]
        else:
            B=B[2:4]
        bg_color="#"+R+G+B
        
def rending_env():
    #draw ocean backgrounds
    draw_bg()
    
    #draw cat position at the middle of screen    
    helpers.make_creature(canvas, (window_width/2, window_height/2),width=cat_width,tag='cat')
    
    #draw stone and water grass with random position, size and styles.
    for i in range(no_watergrass):
        land_x.append(random.randint(100,window_width-100))#x position at a random range form 100 to window_width-100
        land_y.append(random.randint(window_height-400,window_height-200))#y position at a random range from window_height-400 to window_height-200 (relatively bottom of the screen)
        land_size.append(random.randint(200,500))#size at a random range from 200 to 500
        helpers.make_landscape_object(canvas,(land_x[-1],land_y[-1]),size=land_size[-1],tag=f'watergrass{i}')
        #tag name using python format string. same techniques applied to fish names as well.
        #Reference:
        #3. python format string: https://stackoverflow.com/questions/4928526/python-format-string
    
    #draw fish with various colors, size, direction(heading), position
    for i in range(no_fish):
        fish_startx.append(random.randint(100,window_width-100))
        fish_starty.append(random.randint(100,window_height-100))
        fish_head.append(random.choice(['left','right']))
        fish_color.append(random.choice(colors))
        fish_size.append(random.choice(size_of_fish))
        fish_alive.append(1)
        helpers.make_fish(canvas,(fish_startx[-1],fish_starty[-1]),fish_size[-1],
                          fish_head[-1],color=fish_color[-1],tag=f'fish{i}')


def make_cat(event):
    canvas.delete('pop')
    helpers.make_creature(canvas, (event.x, event.y),width=cat_width,tag='cat')
    gui.update()

def make_pop_cat(event):    
    global eat_tag
    try:
        shape_ids = canvas.find_overlapping(
            event.x - 1, 
            event.y - 1, 
            event.x + 1, 
            event.y + 1)
        shape_id = shape_ids[-1] # get the top shape
        current_tag = canvas.gettags(shape_id)
        eat_tag = current_tag[0]
    except:
        eat_tag = None
    canvas.delete('cat')
    helpers.make_creature_pop(canvas, (event.x, event.y),width=cat_width,tag='pop')
    if eat_tag[0:4]=='fish':
        fishid=int(eat_tag[4:])
        canvas.delete(eat_tag)
        fish_alive[fishid]=0
        cat_grow(fish_size[fishid])
    gui.update()
    
def move_fish(fishid):
    if fish_alive[fishid]==1:
        if fish_head[fishid]=='left':
            sign=-1
        else:
            sign=1
        x=sign*random.randint(1,3)*fish_size[fishid]/25#horizontal speed of fish is 
        if random.random()<0.3:#rotate the fish moving direction with a probability of 0.3 
            rotate_degree=random.uniform(-1.5,1.5)#rotate angle should be small per frame
            utilities.rotate(canvas,f'fish{fishid}',rotate_degree)  

        #When fish move to the boundaries of the screen, bounce it off with an opposite heading                          
        if fish_startx[fishid]>window_width:
            canvas.delete(f'fish{fishid}')
            fish_head[fishid]='left'
            helpers.make_fish(canvas,(fish_startx[fishid],fish_starty[fishid]),
                              fish_size[fishid],fish_head[fishid],color=fish_color[fishid],tag=f'fish{fishid}')
        elif fish_startx[fishid]<0:
            canvas.delete(f'fish{fishid}')
            fish_head[fishid]='right'
            helpers.make_fish(canvas,(fish_startx[fishid],fish_starty[fishid]),
                              fish_size[fishid],fish_head[fishid],color=fish_color[fishid],tag=f'fish{fishid}')      
        utilities.update_position(canvas,f'fish{fishid}',x,0)
        fish_startx[fishid]+=x#fish rotation angles are small so just add up x to update x position.

def select_features(event):
    #modified from the code in demos
    global active_tag
    try:
        shape_ids = canvas.find_overlapping(
            event.x - 1, 
            event.y - 1, 
            event.x + 1, 
            event.y + 1)
        shape_id = shape_ids[-1] # get the top shape
        current_tag = canvas.gettags(shape_id)
        active_tag = current_tag[0]
    except:
        active_tag = None
            
def move_features(event):
    #modified from the code in demos
    if not active_tag:
        print('no tag selected')
        return
    
    # calculate the current position of the current shape:
    width = utilities.get_width(canvas, active_tag)
    height = utilities.get_height(canvas, active_tag)
    left = utilities.get_left(canvas, active_tag) 
    top = utilities.get_top(canvas, active_tag) 
    current_x = left + (width / 2)
    current_y = top + (height / 2)

    # calculate the delta of the current shape:
    delta_x = -1 * (current_x - event.x)
    delta_y = -1 * (current_y - event.y)

    # move the shape:
    if active_tag[0:4]!='ocea' and active_tag[0:4]!='fish':
        utilities.update_position(canvas, active_tag, x=delta_x, y=delta_y)
    if active_tag[0:4]=='fish':
        fishid=int(active_tag[4:])
        if fish_alive[fishid]==1:
            utilities.update_position(canvas, active_tag, x=delta_x, y=delta_y)
            fish_startx[fishid]+=delta_x
            fish_starty[fishid]+=delta_y

def delete_features(event):
    #modifed from the code in demos
    global delete_tag
    try:
        shape_ids = canvas.find_overlapping(
            event.x - 1, 
            event.y - 1, 
            event.x + 1, 
            event.y + 1)
        shape_id = shape_ids[-1] # get the top shape
        current_tag = canvas.gettags(shape_id)
        delete_tag = current_tag[0]
    except:
        delete_tag = None      
    if delete_tag!=None:
        if delete_tag[0:4]!='ocea':
            if delete_tag[0:4]=='fish':
                fishid=int(delete_tag[4:])
                fish_alive[fishid]=0
            canvas.delete(delete_tag)
            
def add_fish(event):
    #right click to add a fish
    global no_fish
    fish_startx.append(event.x)
    fish_starty.append(event.y)
    fish_head.append(random.choice(['left','right']))
    fish_color.append(random.choice(colors))
    fish_size.append(random.choice(size_of_fish))
    fish_alive.append(1)
    helpers.make_fish(canvas,(fish_startx[-1],fish_starty[-1]),fish_size[-1],
                      fish_head[-1],color=fish_color[-1],tag=f'fish{no_fish}')
    no_fish+=1

def add_fish_by_period():
    #add a fish periodically
    global no_fish
    fish_startx.append(random.randint(100,window_width-100))
    fish_starty.append(random.randint(100,window_height-100))
    fish_head.append(random.choice(['left','right']))
    fish_color.append(random.choice(colors))
    fish_size.append(random.choice(size_of_fish))
    fish_alive.append(1)
    helpers.make_fish(canvas,(fish_startx[-1],fish_starty[-1]),fish_size[-1],
                      fish_head[-1],color=fish_color[-1],tag=f'fish{no_fish}')
    no_fish+=1
    
def calc_fish_alive():
    #Calulate how many fish currently alive on aquarium
    return sum(fish_alive)#alive fish is marked as 1, removed/eaten fish is marked as 0, so the sum of the elements in the list is the number of fish alive.

def ending_animation():
    #An ending animation for the end of the game. The cat is poping and rotating from its originally size to the final size.
    canvas.delete('cat')
    canvas.delete('pop')
    tag='cat'
    helpers.make_creature(canvas,(window_width/2,window_height/2),width=100,tag=tag)
    width_step=(cat_width-100)/100
    frames=50
    for i in range(frames):
        canvas.delete(tag)
        if i%5==0:
            if tag=='cat':
                tag='pop'
            else:
                tag='cat'
        if tag=='cat':
            helpers.make_creature(canvas,(window_width/2,window_height/2),width=100+i*width_step,tag=tag)
        else:
            helpers.make_creature_pop(canvas,(window_width/2,window_height/2),width=100+i*width_step,tag=tag)            
        utilities.rotate(canvas,tag,degrees=360/(frames-1)*i*4,origin=(window_width/2,window_height/2))
        gui.update()
        time.sleep(1/25)

def keep_poping():
    #Make the cat keep poping
    canvas.delete('cat')
    canvas.delete('pop')
    tag='cat'
    while(1):
        canvas.delete(tag)
        if tag=='cat':
            tag='pop'
        else:
            tag='cat'
        if tag=='cat':
            helpers.make_creature(canvas,(window_width/2,window_height/2),width=cat_width,tag=tag)
        else:
            helpers.make_creature_pop(canvas,(window_width/2,window_height/2),width=cat_width,tag=tag)            
        gui.update()
        time.sleep(1/5)    
        
def display_info(frame):
    #Display the info of game status.
    #Reference:
    #1. How to add a Tkinter Text in canvas: https://stackoverflow.com/questions/28518976/how-to-add-a-tkinter-text-variable-in-canvas-text
    canvas.create_text(window_width/2,30,text='%.2f'%(run_time-frame/25),font=('Ink Free',30),tag='text')
    canvas.create_text(140,80,text='fish number: %02d'%(calc_fish_alive()),font=('Ink Free',30),tag='text')
    canvas.create_text(140,110,text='fish ate: %02d'%(fish_eaten),font=('Ink Free',30),tag='text')
    canvas.create_text(140,140,text='cat width: %02d'%(cat_width),font=('Ink Free',30),tag='text')   
    
def main():
    rending_env()
    canvas.bind(MOUSE_CLICK,make_pop_cat)
    canvas.bind(MOUSE_RELEASE,make_cat)
    canvas.bind(MOUSE_WHEEL_MOTION,move_features)
    canvas.bind(MOUSE_WHEEL_CLICK,select_features)
    canvas.bind(RIGHT_CLICK,add_fish)
    canvas.bind(DOUBLE_CLICK,delete_features)
    for i in range(total_frames):
        display_info(i)        
        if i%add_fish_frame==0:
            add_fish_by_period()
        for j in range(no_fish):
            if fish_alive[j]==1:
                move_fish(j)
        gui.update()
        time.sleep(sleep_time)
        canvas.delete('text')
    #game end
    canvas.unbind(MOUSE_CLICK)
    canvas.unbind(MOUSE_RELEASE)
    canvas.unbind(MOUSE_WHEEL_MOTION)
    canvas.unbind(MOUSE_WHEEL_CLICK)
    canvas.unbind(RIGHT_CLICK)
    canvas.unbind(DOUBLE_CLICK)
    ending_animation()
    canvas.create_text(window_width/2,window_height/6,text='Hope you enjoy the game! Your pop cat have ate %d fishes! Fat as a width of %d!'%(fish_eaten,cat_width),
                       font=('Ink Free',30),tag='text',fill='white')
    keep_poping()
#Reference
# 1. Why you should add if __name__ == '__main__': main() to all your python program: https://stackoverflow.com/questions/419163/what-does-if-name-main-do    
if __name__ == '__main__':    
    main()
########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()