import time
 
def calculate_fps(prev_time):
    current_time = time.time()     

    if prev_time ==  0:
        fps = 0      
  
    else: 
        fps = 1 / (current_time - prev_time)

    
    
    
    prev_time  =  current_time

    return fps, prev_time