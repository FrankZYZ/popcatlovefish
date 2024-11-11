import utilities
import random
def get_bias():
    return random.choice([-1,1])*random.randint(10,50)

def relocate_scale(vector,center,width,obj_name):
    if obj_name=='cat':
        prefix=[44,85]
        scale=width/110
    elif obj_name=='grass':
        prefix=[127,237]
        scale=width/496
    elif obj_name=='fish':
        prefix=[133,117]
        scale=width/315
    for i in range(len(vector)):
        vector[i]=(float(vector[i][0]-prefix[0])*scale+center[0],float(vector[i][1]-prefix[1])*scale+center[1])
    return vector

def make_creature(canvas, center, tag='creature', color='#BDA797',width=110):
    catbody=[(22,2),(50,20),(75,24),(93,15),(114,8),(118,33),(110,43),(105,60),
           (96,84),(100,103),(105,118),(109,130),(88,130),(56,130),(30,130),(4,130),
           (8,110),(12,88),(3,67),(2,51),(15,38),(13,21)]
    catface=[(12,55),(16,45),(27,33),(36,25),(47,20),(60,27),(73,36),(73,42),
             (75,47),(64,53),(49,57),(37,58),(24,54),(19,52)]
    cateye1=[(22,34),(27,32),(33,34),(32,38),(30,42),(26,44),(21,42)]
    cateye2=[(52,44),(56,37),(65,36),(72,42),(63,46)]
    eyespark1=[(29,35),(28,36),(29,37)]
    eyespark2=[(60,40),(62,39),(63,40)]
    catnose=[(34,56),(31,51),(28,49),(35,48),(42,51),(37,53)]
    catjaw=[(29,64),(31,65),(33,66)]
    catear1=[(33,26),(33,19),(30,7),(42,14),(45,20)]
    catear2=[(57,22),(62,21),(74,25),(92,16),(89,27),(86,36),(76,28),(62,23)]
    catchin1=[(3,52),(10,43),(11,48)]
    catchin2=[(79,48),(93,61),(101,53),(100,68),(91,87),(83,80),(85,72),(81,61)]
    
    catbody=relocate_scale(catbody,center,width,'cat')
    cateye1=relocate_scale(cateye1,center,width,'cat')
    cateye2=relocate_scale(cateye2,center,width,'cat')
    catface=relocate_scale(catface,center,width,'cat')
    catnose=relocate_scale(catnose, center, width,'cat')
    eyespark1=relocate_scale(eyespark1, center, width,'cat')
    eyespark2=relocate_scale(eyespark2, center, width,'cat')
    catjaw=relocate_scale(catjaw, center, width,'cat')
    catear1=relocate_scale(catear1, center, width,'cat')
    catear2=relocate_scale(catear2, center, width,'cat')
    catchin1=relocate_scale(catchin1, center, width,'cat')
    catchin2=relocate_scale(catchin2, center, width,'cat')
    
    canvas.create_polygon(catbody,width=2,fill=color,smooth='True',tag=tag)
    canvas.create_polygon(catface,width=2,fill='#F0F0F0',smooth='True',tag=tag)
    canvas.create_polygon(cateye1,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(cateye2,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catnose,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_line(eyespark1,smooth=True,fill='white',width=width/110,tag=tag)
    canvas.create_line(eyespark2,smooth=True,fill='white',width=width/110,tag=tag)
    canvas.create_line(catjaw,smooth=True,fill='#515151',width=width/55,tag=tag)
    canvas.create_polygon(catear1,width=2,fill='#AA7F6F',smooth='True',tag=tag)
    canvas.create_polygon(catear2,width=2,fill='#A07166',smooth='True',tag=tag)
    canvas.create_polygon(catchin1,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catchin2,width=2,fill='#515151',smooth='True',tag=tag)

def make_creature_pop(canvas, center, tag='creature', color='#BDA797',width=110):
    
    catbody=[(22,2),(50,20),(75,24),(93,15),(114,8),(118,33),(110,43),(105,60),
           (96,84),(100,103),(105,118),(109,130),(88,130),(56,130),(30,130),(4,130),
           (8,110),(12,88),(3,67),(2,51),(15,38),(13,21)]
    catface=[(15,46),(21,38),(31,30),(48,22),(65,24),(76,29),(82,34),(88,43),
             (85,51),(79,50),(67,42),(53,36),(45,32),(27,40)]
    cateye1=[(22,35),(30,29),(39,30),(33,35)]
    cateye2=[(65,36),(71,34),(77,36),(80,39),(73,40)]
    catnose=[(34,56),(31,51),(28,49),(35,48),(42,51),(37,53)]
    catjaw=[(9,64),(10,55),(22,42),(30,37),(39,35),(50,35),(65,39),(77,47),
            (84,59),(87,72),(80,88),(68,98),(55,101),(40,99),(22,89),(13,75)]
    catear1=[(33,26),(33,19),(30,7),(42,14),(45,20)]
    catear2=[(57,22),(62,21),(74,25),(92,16),(89,27),(86,36),(76,28),(62,23)]
    catchin1=[(3,52),(10,43),(11,48)]
    catchin2=[(85,48),(99,61),(107,53),(104,68),(97,87),(89,80),(90,72),(85,61)]
    cattongue=[(87,72),(80,88),(68,98),(55,101),(40,99),(22,89),(13,75)]
    
    catbody=relocate_scale(catbody,center,width,'cat')
    cateye1=relocate_scale(cateye1,center,width,'cat')
    cateye2=relocate_scale(cateye2,center,width,'cat')
    catface=relocate_scale(catface,center,width,'cat')
    catnose=relocate_scale(catnose, center, width,'cat')
    catjaw=relocate_scale(catjaw, center, width,'cat')
    catear1=relocate_scale(catear1, center, width,'cat')
    catear2=relocate_scale(catear2, center, width,'cat')
    catchin1=relocate_scale(catchin1, center, width,'cat')
    catchin2=relocate_scale(catchin2, center, width,'cat')
    cattongue=relocate_scale(cattongue, center, width,'cat')
    
    canvas.create_polygon(catbody,width=2,fill=color,smooth='True',tag=tag)
    canvas.create_polygon(catface,width=2,fill='#F0F0F0',smooth='True',tag=tag)
    canvas.create_polygon(cateye1,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(cateye2,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catnose,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catjaw,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catear1,width=2,fill='#AA7F6F',smooth='True',tag=tag)
    canvas.create_polygon(catear2,width=2,fill='#A07166',smooth='True',tag=tag)
    canvas.create_polygon(catchin1,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(catchin2,width=2,fill='#515151',smooth='True',tag=tag)
    canvas.create_polygon(cattongue,width=2,fill='#DDAAAA',smooth='True',tag=tag)

def make_fish(canvas,center,width,head,tag='Fish',color='orange'):
    if head=="left":
        fish_body=[(1,119),(13,91),(38,60),(77,31),(117,17),(166,23),
                   (209,47),(240,75),(261,100),(285,86),(312,77),
                   (312,107),(290,123),(295,150),(286,175),(165,147),
                   (253,127),(233,151),(203,171),(174,186),(138,199),
                   (95,198),(53,182),(23,160)]
        fish_eye_outer=[(13,86),(80,145)]
        fish_eye=[(25,110),(52,133)]
        fish_eye_spark=[(30,117),(40,124)]
        fish_fin=[(82,120),(96,107),(111,98),(117,114),(118,134),(112,145),
                  (96,137)]
        fish_gill_1=[(128,71),(133,81),(127,94)]
        fish_gill_2=[(138,71),(143,81),(137,94)]
        fish_gill_3=[(148,71),(153,81),(147,94)]
    else:
        fish_body=[(313-1,119),(313-13,91),(313-38,60),(313-77,31),(313-117,17),(313-166,23),
                   (313-209,47),(313-240,75),(313-261,100),(313-285,86),(313-312,77),
                   (313-312,107),(313-290,123),(313-295,150),(313-286,175),(313-165,147),
                   (313-253,127),(313-233,151),(313-203,171),(313-174,186),(313-138,199),
                   (313-95,198),(313-53,182),(313-23,160)]
        fish_eye_outer=[(313-13,86),(313-80,145)]
        fish_eye=[(313-25,110),(313-52,133)]
        fish_eye_spark=[(313-30,117),(313-40,124)]
        fish_fin=[(313-82,120),(313-96,107),(313-111,98),(313-117,114),(313-118,134),(313-112,145),
                  (313-96,137)]
        fish_gill_1=[(313-128,71),(313-133,81),(313-127,94)]
        fish_gill_2=[(313-138,71),(313-143,81),(313-137,94)]
        fish_gill_3=[(313-148,71),(313-153,81),(313-147,94)]
        
    fish_body=relocate_scale(fish_body,center,width,'fish')
    fish_eye_outer=relocate_scale(fish_eye_outer,center,width,'fish')
    fish_eye=relocate_scale(fish_eye,center,width,'fish')
    fish_eye_spark=relocate_scale(fish_eye_spark,center,width,'fish')
    fish_fin=relocate_scale(fish_fin,center,width,'fish')
    fish_gill_1=relocate_scale(fish_gill_1,center,width,'fish')
    fish_gill_2=relocate_scale(fish_gill_2,center,width,'fish')
    fish_gill_3=relocate_scale(fish_gill_3,center,width,'fish')

    canvas.create_polygon(fish_body,width=width/100,fill=color,smooth='True',outline='black',tag=tag)
    canvas.create_oval(fish_eye_outer,fill='white',outline='',tag=tag)
    canvas.create_oval(fish_eye,fill='black',tag=tag)
    canvas.create_oval(fish_eye_spark,fill='white',tag=tag)
    canvas.create_polygon(fish_fin,width=width/100,fill='pink',outline='black',smooth='True',tag=tag)  
    canvas.create_line(fish_gill_1,smooth=True,fill='black',width=width/100,tag=tag)
    canvas.create_line(fish_gill_2,smooth=True,fill='black',width=width/100,tag=tag)
    canvas.create_line(fish_gill_3,smooth=True,fill='black',width=width/100,tag=tag)

def make_landscape_object(canvas, position, size=100,tag='Landscape'):
    colors=['#22B14C','#0E4E11','#2EFF09','#A8D244']
    rock=[(57+get_bias()/2,370),(27+get_bias()/2,403),(71+get_bias()/2,447),(153+get_bias()/2,437),(185+get_bias()/2,407)]
    rock=relocate_scale(rock, position, size, 'grass')
    for i in range(random.randint(4,8)):
        seaweed1=[(18+get_bias()*2,122),(23+get_bias()*2,146),
                  (5+get_bias(),187),(27+get_bias(),253),
                  (9+get_bias(),333),(61,389)]    
        seaweed1=relocate_scale(seaweed1, position, size, 'grass')
        canvas.create_line(seaweed1,width=random.randint(5,15)*size/496,smooth=True,tag=tag,fill=random.choice(colors))
    canvas.create_polygon(rock,width=2,fill='gray',smooth='True',tag=tag)
    
