import os
import yaml

#suppress tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)



LANGUAGE = config['language']


'''
TODO: 
MAKE CONFIGURABLE INSTALLATION SCRIPT:
    INSTALLS THE REQUIRED PACKAGES
    
'''
 