import os
import shutil
import random

if __name__ == '__main__':

    source_dir = 'D:/Dataset/removebg_80_sad'
    target_dir = 'D:/Dataset/removebg_20_sad'

    
    for idx, file in enumerate(random.sample(os.listdir('D:/Dataset/removebg_80_sad'),20)):
        shutil.copy2(os.path.join(source_dir,file),os.path.join(target_dir,file))
        os.remove(os.path.join(source_dir,file))
        
                        
